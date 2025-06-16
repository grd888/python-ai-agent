
import os
import subprocess


def run_python_file(working_directory, file_path):
  # Check if file_path is outside the working directory
  abs_working_dir = os.path.abspath(working_directory)
  abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
  
  if not abs_file_path.startswith(abs_working_dir):
    return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
  if not os.path.exists(abs_file_path):
    return f'Error: File "{file_path}" not found.'
  
  if not abs_file_path.endswith('.py'):
    return f'Error: "{file_path}" is not a Python file.'
  
  try:
    # Run the Python file with subprocess, capturing stdout and stderr
    result = subprocess.run(
      ['python', abs_file_path],
      capture_output=True,
      text=True,
      timeout=30,
      cwd=working_directory
    )
    
    # Format the output
    stdout = result.stdout.strip()
    stderr = result.stderr.strip()
    
    output_parts = []
    
    if stdout:
      output_parts.append(f"STDOUT:\n{stdout}")
    
    if stderr:
      output_parts.append(f"STDERR:\n{stderr}")
    
    if result.returncode != 0:
      output_parts.append(f"Process exited with code {result.returncode}")
    
    if not output_parts:
      return "No output produced."
    
    return "\n\n".join(output_parts)
    
  except subprocess.TimeoutExpired:
    return f"Error: executing Python file: Timeout expired (30 seconds)"
  except Exception as e:
    return f"Error: executing Python file: {e}"