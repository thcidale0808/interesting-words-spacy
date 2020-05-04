import click, logging, os
from app import ProcessExecutor

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logging.basicConfig(level=LOGLEVEL)

@click.command()
@click.option(
    '--input',
    required=True,
    help='Path to the files that will be processed.'
)
@click.option(
    '--output',
    required=True,
    help='Path to the interesting word report file.'
)
def main(input, output):
    """
    CLI for generating a report of interesting words for your files
    """
    try:
        logging.info("Process started")
        
        #create process executor
        executor = ProcessExecutor()
        
        #generate the report for input and output
        executor.generate_report(input, output)

    except Exception as e:
        logging.error(e)
    finally:
        logging.info("Process finished")
    
if __name__ == "__main__":
    main()
