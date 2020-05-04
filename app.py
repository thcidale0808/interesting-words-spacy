import os,csv, logging
from documents import DocumentWizard

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logging.basicConfig(level=LOGLEVEL)

class ProcessExecutor:
    
    def generate_report(self, input_path:str, output_path:str) -> None:
        """
        Save on output folder all interest words reports for each file from input folder
        """
        # List all files from input folder
        for entry in os.listdir(input_path):
            
            full_input_path = os.path.join(input_path, entry)
            
            logging.debug(f'Start to process file: {full_input_path}')    
            #check if they entry if a valid file
            if os.path.isfile(full_input_path):
                
                #initialize document wizard class for file
                document_wizard = DocumentWizard(full_input_path)
                
                #get all interesting words from file
                result = document_wizard.find_interesting_words()
                
                logging.debug(f'{len(result)} interesting words found')
                
                #define output full path and save the list of dictionaries to csv
                full_output_path = os.path.join(output_path,f'{os.path.splitext(entry)[0]}_report.csv')
                
                self.save_file(full_output_path, result)

                logging.debug(f'Finished process file: {full_input_path}')
   
    def save_file(self, full_output_path:str, result:list) -> None:
        """
        Save dictonary to csv
        """
        if len(result) > 0:
            #define csv header
            keys = result[0].keys()
            
            #create folder in case it doesn't exist
            os.makedirs(os.path.dirname(full_output_path), exist_ok=True)
            
            #create and write all dictionary content to csv file
            with open(full_output_path, 'w') as output_file:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(result)
