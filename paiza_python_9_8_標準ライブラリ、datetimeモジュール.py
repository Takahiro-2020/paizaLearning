# datetime���W���[���ɂ���datetime�N���X���C���|�[�g
from datetime import datetime, timedelta, timezone

# now�̓N���X���\�b�h�Ȃ̂ŃC���X�^���X����Ȃ�
# datetime�͋��萢�E�� : ���{���� - 9����
today = datetime.now()
print(today)

# timezone�N���X�œ��{�����̃^�C���]�[�����C���X�^���X���@aware
# timedelta�N���X�Ŏ�����\��
jst   = timezone(timedelta(hours=9))
today = datetime.now(jst)
print(today)
print(today.year)
print(today.month)
print(today.day)

# �������w�肵��datetime�C���X�^���X
# ���t�A����
day = datetime.strptime("2030/01/10 06:02:19", "%Y/%m/%d %H:%M:%S")
print(day)