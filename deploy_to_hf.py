"""Deploy Epoch.ai to HuggingFace Spaces."""

import os
import sys

# === CONFIGURATION ===
HF_TOKEN = os.getenv("HF_TOKEN", "")
SPACE_NAME = "epoch-ai"  # Will create: krithickvivek/epoch-ai
SPACE_SDK = "docker"

# Files/dirs to skip when uploading
SKIP = {
    ".venv", "__pycache__", ".pytest_cache", ".claude", ".git",
    "cookies.txt", "tempcookies5.txt", "deploy_to_hf.py",
    "test_hf.py", "test_hf2.py", ".env",
}
SKIP_EXT = {".pyc", ".pyo", ".db"}


def main():
    from huggingface_hub import HfApi, create_repo

    api = HfApi(token=HF_TOKEN)

    # 1. Verify token
    print("Verifying token...")
    try:
        user_info = api.whoami()
        username = user_info["name"]
        print(f"  Logged in as: {username}")
    except Exception as e:
        print(f"  ERROR: Token verification failed: {e}")
        print("  Please create a token with 'Write' permission at https://huggingface.co/settings/tokens")
        sys.exit(1)

    repo_id = f"{username}/{SPACE_NAME}"

    # 2. Create the Space (or use existing)
    print(f"\nCreating Space: {repo_id} ...")
    try:
        create_repo(
            repo_id=repo_id,
            repo_type="space",
            space_sdk=SPACE_SDK,
            token=HF_TOKEN,
            exist_ok=True,
            private=False,
        )
        print(f"  Space ready: https://huggingface.co/spaces/{repo_id}")
    except Exception as e:
        print(f"  ERROR creating Space: {e}")
        print("  Make sure your token has write access.")
        sys.exit(1)

    # 3. Upload the project folder
    project_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"\nUploading project from: {project_dir}")

    try:
        api.upload_folder(
            folder_path=project_dir,
            repo_id=repo_id,
            repo_type="space",
            token=HF_TOKEN,
            ignore_patterns=[
                ".venv/**",
                "__pycache__/**",
                ".pytest_cache/**",
                ".claude/**",
                ".git/**",
                "*.pyc",
                "*.pyo",
                "*.db",
                "cookies.txt",
                "tempcookies*.txt",
                "deploy_to_hf.py",
                "test_hf*.py",
                ".env",
                "data/*.db",
            ],
            commit_message="Deploy Epoch.ai - AI-powered placement preparation platform",
        )
        print(f"\n  Upload complete!")
        print(f"\n  Your Space: https://huggingface.co/spaces/{repo_id}")
        print(f"  It will take 2-5 minutes to build the Docker image and start.")
    except Exception as e:
        print(f"  ERROR uploading: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
