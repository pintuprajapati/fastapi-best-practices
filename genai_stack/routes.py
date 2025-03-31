from fastapi import APIRouter, UploadFile, File, BackgroundTasks, HTTPException, Depends, Query
from typing import List, Dict, Any

# Import AI stack components
from genai_stack import DocumentProcessor, TextChunker, EmbeddingGenerator, VectorStore, QueryProcessor, process_document
from models.document import Document
from models.query import SearchResult
from utils import create_response
import custom_log as log

router = APIRouter(prefix="/ai", tags=["ai"])

# Initialize AI stack components
document_processor = DocumentProcessor()
text_chunker = TextChunker()
embedding_generator = EmbeddingGenerator()
vector_store = VectorStore()
query_processor = QueryProcessor(embedding_generator, vector_store)

@router.post("/documents/upload", response_model=Dict[str, Any])
async def upload_document(file: UploadFile = File(...)):
    """Upload a document for processing"""
    try:
        document = await document_processor.upload_document(file)
        
        # Start processing task in background
        # process_document.delay(document.dict())
        
        result_data = {
            "document_id": document.id
        }
        
        log.set_logger("upload_document", f"Document uploaded and queued for processing", action="info")
        return create_response(message="Document uploaded and queued for processing", status_code=200, success=True, data=result_data)
    except Exception as e:
        log.set_logger("upload_document", f"Error uploading document: {str(e)}", action="error")
        return create_response(message="Something went wrong while uploading a document", status_code=500, success=False, data={})

@router.get("/query", response_model=Dict[str, Any])
async def query_documents(q: str = Query(..., description="Query text"), top_k: int = Query(5, description="Number of results to return")):
    """Query the document database"""
    try:
        log.set_logger("query", f"User query: {q}", action="info")
        search_results = await query_processor.process_query(q, top_k=top_k)
        response = query_processor.format_response(search_results)
        
        result_data = {
            "query": q,
            "results": [result.dict() for result in search_results],
            "response": response
        } 
        
        log.set_logger("query", f"Result fetched successfully", action="info")
        return create_response(message="Result fetched successfully", status_code=200, success=True, data=result_data)
    except Exception as e:
        log.set_logger("query", f"Error while getting the result for the query: {str(e)}", action="error")
        return create_response(message="Something went wrong while getting answer for the query", status_code=500, success=False, data={})