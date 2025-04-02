# 🚀 How to Use This Genai-Stack Boilerplate

This guide provides step-by-step instructions on how to clone this boilerplate repository and start your own project with a fresh Git history.

## 📌 Steps to Get Started

### 1️⃣ Clone the Boilerplate Repository  
Replace `branch-name` with the branch you want to use and `git-branch-url` with the repository URL.

```sh
git clone --depth 1 --branch branch-name git-branch-url new-dir-name
```
This clones only the latest version of the specified branch into `new-dir-name`.

#### Example:
```sh
git clone --depth 1 --branch genai_stack https://github.com/pintuprajapati/fastapi-best-practices.git Rag-App
```
This clones only the latest commit of the `genai_stack` branch into the `Rag-App` directory.

### 2️⃣ Navigate to the Project Directory  
```sh
cd new-dir-name
```

### 3️⃣ Remove the Existing Git History  
```sh
rm -rf .git
```
This ensures your project is independent of the boilerplate's commit history.

#### Example:
```sh
cd Rag-App
rm -rf .git
```
This removes the `.git` directory inside `Rag-App`, allowing you to start with a fresh Git history.

### 4️⃣ Initialize a New Git Repository  
```sh
git init
```

### 5️⃣ (Optional) Configure User Details  
If you want commits to be linked to a specific Git account, modify the `.git/config` file:

```sh
[user]
    email = your-email
    name = your-username
```

Alternatively, you can set it via CLI:
```sh
git config user.email "your-email"
git config user.name "your-username"
```

### 6️⃣ Add and Commit the Code  
```sh
git add .
git commit -m "Initial commit"
```

### 7️⃣ Set Up a New GitHub Repository  
Replace `git-branch-url` with your new repository URL.

```sh
git branch -M main  # Change 'main' to 'your-branch-name' if needed
git remote add origin git-branch-url
git push -u origin main  # Change 'main' if needed
```

🎉 **That's it! You're now ready to start your project using this boilerplate!** 🚀  
For any issues or improvements, feel free to contribute. Happy coding! 👨‍💻🔥

