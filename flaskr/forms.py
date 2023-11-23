from wtforms.form import Form
from wtforms.fields import (
    StringField, FileField, PasswordField, SubmitField, HiddenField, TextAreaField
)
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_login import current_user
from flask import flash

from flaskr.models import User, UserConnect

# ログイン用のForm
class LoginForm(Form):
    email = StringField('メール:', validators=[DataRequired(), Email()]
    )
    password = PasswordField('パスワード：', validators=[DataRequired(), EqualTo('confirm_password', message= 'パスワードが一致しません')]
    )
    confirm_password = PasswordField('パスワード再入力:', validators=[DataRequired()]
    )
    submit = SubmitField('ログイン')


# 登録用のForm
class RegisterForm(Form):
    email = StringField(
        'メール：', validators=[DataRequired(), Email('メールアドレスが誤っています')]
    )
    username = StringField('名前：', validators=[DataRequired()])
    submit = SubmitField('登録')

    def validate_email(self, field):
        if User.select_user_by_email(field.data):
            raise ValidationError('メールアドレスはすでに登録されています')

# パスワード設定用のform
class ResetPasswordForm(Form):
    password = PasswordField(
        'パスワード',
        validators=[DataRequired(), EqualTo('confirm_password', message='パスワードが一致しません。')]
    )
    confirm_password = PasswordField(
        'パスワード確認：', validators=[DataRequired()]
    )
    submit = SubmitField('パスワードを更新する')
    def validate_password(self, field):
        if len(field.data) < 8:
            raise ValidationError('パスワードは8文字以上です')

class ForgotPasswordForm(Form):
    email = StringField('メール：', validators=[DataRequired(), Email()])
    submit = SubmitField('パスワードを再設定する')

    def validate_email(self, field):
        if not User.select_user_by_email(field.data):
            raise ValidationError ('そのメールアドレスは存在しません')

# ユーザ情報編集のForm
class UserForm(Form):
    email = StringField('メール:', validators=[DataRequired(), Email('メールアドレスが誤っています')])
    username = StringField('名前:', validators=[DataRequired()])
    header = TextAreaField('ヘッダー:')
    footer = TextAreaField('フッター:')
    picture_path = FileField('ファイルアップロード')
    submit = SubmitField('登録情報更新')

    def validate(self):
        if not super(Form, self).validate():
            return False
        user = User.select_user_by_email(self.email.data)
        if user:
            if user.id != int(current_user.get_id()):
                flash('そのメールアドレスは既に登録されています')
                return False
        return True

#パスワード変更フォーム
class ChangePasswordForm(Form):
    password = PasswordField(
        'パスワード',
        validators=[DataRequired(), EqualTo('confirm_password', message='パスワードが一致しません。')]
    )
    confirm_password = PasswordField(
        'パスワード確認：', validators=[DataRequired()]
    )
    submit = SubmitField('パスワードの更新')
    def validate_password(self, field):
        if len(field.data) < 8:
            raise ValidationError('パスワードは8文字以上です')

# ユーザ検索
class UserSearchForm(Form):
    username = StringField('名前: ' , validators=[DataRequired()])
    submit = SubmitField('ユーザ検索')

# 友達申請
class ConnectForm(Form):
    connect_condition = HiddenField()
    to_user_id = HiddenField()
    submit = SubmitField()

# メッセージ作成
class MessageForm(Form):
    to_user_id = HiddenField()
    message = TextAreaField()
    submit = SubmitField('メッセージ送信')

    def validate(self):
        if not super(Form, self).validate():
            return False
        is_friend = UserConnect.is_friend(self.to_user_id.data)
        if not is_friend:
            return False
        return True

# メール作成フォーム
class MailForm(Form):
    to_email = TextAreaField('メールアドレス')
    mail_topic = TextAreaField('件名')
    header = TextAreaField('ヘッダー')
    mail_message = TextAreaField('本文※メール作成後クリップボードにコピーされます。')
    footer = TextAreaField('フッター')
    submit = SubmitField('メール作成')

# ユーザ削除 
class DeleteForm(Form):
    password = PasswordField(
        'パスワード',
        validators=[DataRequired(), EqualTo('confirm_password', message='パスワードが一致しません。')]
    )
    confirm_password = PasswordField(
        'パスワード確認：', validators=[DataRequired()]
    )
    submit = SubmitField('退会')