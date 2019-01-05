from info.modules.passport import passport_bp
from flask import request, abort,current_app
from info.utitils.captcha.captcha import captcha
from info import redis_store
from info import constants


@passport_bp.route('/image_code')
def get_image_code():
    """获取验证码图片的后端接口"""
    """
    1.获取参数
        1.1作为key将验证真是值储存到redis数据库
    2.校验参数
        非空判断code不能为空
    3.逻辑处理
    
    4.获取返回值
    """
    # 作为key将验证真是值储存到redis数据库
    code_id = request.args.get('code_id')
    # 非空判断,ode_id不能为空
    if not code_id:
        current_app.logger.error("参数不足")
        abort(404)
    # 生成验证码图片,验证码图片的真实值

    image_name, real_image_code, image_data = captcha.generate_captcha()
    # code_id作为key将验证码图片的真实值保存到redis数据库,并设置有效时长(5分钟)
    try:
        redis_store.setex("CODEID_%s"%code_id,constants.IMAGE_CODE_REDIS_EXPIRES,real_image_code)
    except Exception as e:
        current_app.logger.error(e)
    # 返回验证图片
    return image_data