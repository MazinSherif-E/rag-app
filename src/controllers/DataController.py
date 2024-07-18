from fastapi import UploadFile
from .BaseController import BaseController
from .ProjectController import ProjectController
from src.models import ResponseSignal
import re
import os

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576
        
    def validate_uploaded_file(self, file: UploadFile): 
        
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED
        
        if file.size > self.app_settings.FILE_MAXIMUM_SIZE * self.size_scale:
            return False, ResponseSignal.FILE_SIZE_SUCCEDED
        
        return True, ResponseSignal.FILE_UPLOADED_SUCCESS 
    
    def generate_unique_filepath(self, original_filename: str, project_id):
        random_key = self.generate_random_string()
        project_path = ProjectController().get_project_path(project_id=project_id)
        
        cleaned_file_name = self.get_clean_filename(original_filename=original_filename)
        
        new_file_path = os.path.join(
            project_path,
            random_key + "_" + cleaned_file_name
        )
        
        while os.path.exists(new_file_path):
            random_key = self.generate_random_string()
            new_file_path = os.path.join(
            project_path,
            random_key + "_" + cleaned_file_name
        )
            
        return new_file_path, random_key + "_" + cleaned_file_name
        
    def get_clean_filename(self, original_filename: str):
        # remove any special characters, except underscore and .
        cleaned_file_name = re.sub(r'[^\w.]', '', original_filename.strip())
        
        # replace spaces with underscore
        cleaned_file_name = cleaned_file_name.replace(" ", "_")
        
        return cleaned_file_name 