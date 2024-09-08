# https://github.com/ultralytics/yolov5/blob/master/utils/general.py#LL79C18-L79C18
def is_jupyter() -> bool:
    # verified on Colab, Jupyterlab, Kaggle, Paperspace.
    try:
        from IPython import get_ipython

        return get_ipython() is not None
    except:
        return False
