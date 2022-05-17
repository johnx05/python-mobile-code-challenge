from features.android.config import driver

def before_feature(context, feature):
    pass


def after_feature(context, feature):
    driver.quit()