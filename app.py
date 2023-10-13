import streamlit as st
import shutil
import os

def rename_images_with_prefix(source_folder_path, destination_folder_path, prefix):
  """Renames images with a prefix in a folder and stores them in a new folder.

  Args:
    source_folder_path: The path to the source folder.
    destination_folder_path: The path to the destination folder.
    prefix: The prefix to add to the new file names.
  """

  # Create the destination folder if it doesn't exist.
  if not os.path.exists(destination_folder_path):
    os.makedirs(destination_folder_path)

  # Iterate over the files in the source folder.
  for file_name in os.listdir(source_folder_path):
    # If the file is an image, rename it and copy it to the destination folder.
    if file_name.endswith('.jpg') or file_name.endswith('.png'):
      new_file_name = f'{prefix}_{file_name}'
      new_file_path = os.path.join(destination_folder_path, new_file_name)
      old_file_path = os.path.join(source_folder_path, file_name)

      # Use the shutil.copyfile() function to copy the file.
      shutil.copyfile(old_file_path, new_file_path)

def rename_images_with_prefix_streamlit():
  """Renames images with a prefix in a folder and stores them in a new folder in Streamlit."""

  # Create a Streamlit app.
  st.title('Rename Images with Prefix')
  findpath = st.file_uploader('choose path')
  system_path=os.getcwd()
  st.write(f'System_path:{system_path}')
  

  # Get the source folder path.
  source_folder_path = st.text_input('Enter the path to the source folder')

  # Get the destination folder path.
  destination_folder_path = st.text_input('Enter the path to the destination folder')

  # Get the prefix.
  prefix = st.text_input('Enter a prefix for the new file names')

  # Rename and copy the images.
  if st.button('Rename Images'):
    rename_images_with_prefix(source_folder_path, destination_folder_path, prefix)

  # Display a message to the user.
  st.success('The images have been renamed and copied to the destination folder.')

if __name__ == '__main__':
  rename_images_with_prefix_streamlit()
