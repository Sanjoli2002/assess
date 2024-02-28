from src.pipeline.pipeline import Prep_Pipeline

if __name__ == "__main__":
    # Instantiate and run the pipeline
    pipeline_instance = Prep_Pipeline()
    clustered_data = pipeline_instance.run_pipeline()

    # Now 'preprocessed_data' contains the preprocessed DataFrame, and you can use it as needed
    print(clustered_data)