"""
This Module hosts functions to interact with Amazon BlazingText, 
a fast implementation of word2vec.
"""
from sagemaker.session import Session, s3_input
from sagemaker.estimator import Estimator
from sagemaker.amazon.amazon_estimator import get_image_uri


def create_blaxing_text_model(
        region_name: str,
        sm_session: Session,
        sm_role: str,
        s3_input_url: str,
        s3_output_url: str):
    """
    Create a BlazingText model.

    Args:
        - region_name: AWS Region Name to use SageMaker in.
        - sm_session: SageMaker Session Object.
        - sm_role: SageMaker role arn that allows SM to connect to s3.
        - s3_input_url: training data input path on s3
        - s3_output_url: model artifacts output path

    Return:
        - bt_model: instance of Estimator, can be used to deploy an inference endpoint
    """
    # define container
    container = get_image_uri(region_name, "blazingtext", "latest")

    # create estimator
    bt_model = Estimator(container,
                         sm_role,
                         train_instance_count=1,
                         train_instance_type='ml.c4.2xlarge',
                         train_volume_size=30,
                         train_max_run=360000,
                         input_mode='File',
                         output_path=s3_output_url,
                         sagemaker_session=sm_session)

    # set hyperparameters
    bt_model.set_hyperparameters(mode="skipgram",
                                 epochs=5,
                                 min_count=5,
                                 sampling_threshold=0.0001,
                                 learning_rate=0.05,
                                 window_size=5,
                                 vector_dim=100,
                                 negative_samples=5,
                                 subwords=True,
                                 min_char=3,
                                 max_char=6,
                                 batch_size=11,
                                 evaluation=True)

    # define data channels
    train_data = s3_input(s3_input_url, distribution='FullyReplicated',
                          content_type='text/plain', s3_data_type='S3Prefix')
    data_channels = {'train': train_data}

    # fit model
    bt_model.fit(inputs=data_channels, logs=True)

    return bt_model
