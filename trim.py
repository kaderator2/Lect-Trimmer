import subprocess
from pathlib import Path

# --- Configuration ---
# Suffix to add to the trimmed video files.
TRIMMED_SUFFIX = "_trimmed"

def trim_video(video_path: Path):
    """
    Trims silence from a single video file using auto-editor.

    Args:
        video_path (Path): The path to the video file to be trimmed.
    """
    # Create the output path, e.g., "lecture1.mp4" -> "lecture1_trimmed.mp4"
    output_path = video_path.with_name(f"{video_path.stem}{TRIMMED_SUFFIX}{video_path.suffix}")

    print(f"  -> Output file will be: {output_path.name}")

    # Command to trim the video using auto-editor.
    # The '-o' flag specifies the output file, avoiding intermediate files.
    command = [
        "auto-editor",
        str(video_path),
        "--no-open",
        "-o",
        str(output_path),
    ]

    try:
        # Execute the command. Using subprocess.run is safer and more modern.
        # It will raise an error if auto-editor fails.
        subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"✅ Successfully trimmed '{video_path.name}'")
    except FileNotFoundError:
        print("\n[ERROR] 'auto-editor' command not found.")
        print("Please make sure auto-editor is installed and accessible in your system's PATH.")
    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] auto-editor failed while processing '{video_path.name}'.")
        print(f"  -> Error: {e.stderr}")
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {e}")

def main():
    """
    Finds and processes all .mp4 files in the current directory.
    """
    current_dir = Path(".")
    
    # Find all .mp4 files that haven't been trimmed yet
    files_to_process = [
        f for f in current_dir.glob("*.mp4") if TRIMMED_SUFFIX not in f.name
    ]

    if not files_to_process:
        print("No new video files to process. ✨")
        return

    total_files = len(files_to_process)
    print(f"🎬 Found {total_files} video(s) to trim.\n")

    for index, file_path in enumerate(files_to_process):
        # The new script handles filenames with spaces automatically.
        print(f"--- Processing file {index + 1}/{total_files}: {file_path.name} ---")
        trim_video(file_path)
        print("-" * 50) # Separator for clarity

    print("\nAll videos processed successfully! 🎉")

if __name__ == "__main__":
    main()
