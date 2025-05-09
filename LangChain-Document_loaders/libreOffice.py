import subprocess
import os

def convert_docx_to_txt(docx_path, output_dir=None):
    if output_dir is None:
        output_dir = os.path.dirname(docx_path)
    
    command = [
        "libreoffice",
        "--headless",
        "--convert-to", "txt:Text",
        "--outdir", output_dir,
        docx_path
    ]

    try:
        subprocess.run(command, check=True)
        print("✅ DOCX converted to TXT successfully.")
        
        txt_path = os.path.join(
            output_dir,
            os.path.splitext(os.path.basename(docx_path))[0] + ".txt"
        )
        
        with open(txt_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()

    except subprocess.CalledProcessError as e:
        print(f"❌ Conversion failed: {e}")
        return None



text = convert_docx_to_txt("/home/vishal/Documents/Documents/Index_Document/Software License Agreement(with Indexing).docx","/home/vishal/LangChain/LangChain-Document_loaders")
print(text[:1000])  # Preview first 1000 chars
