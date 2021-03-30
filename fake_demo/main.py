import json
from faker import Faker
import gooey
from gooey import Gooey, GooeyParser


@Gooey(
    encoding='cp936',
    language='chinese',
    show_success_modal=False,
    program_name='假用户生成',
    program_description='假用户生成，数量中请填写要生成的数量，也可在生成后点击重启按钮重复生成。'
)
def main():
    parser = GooeyParser(description="Faker")
    parser.add_argument('生成数量', action='store', default='1')

    args = parser.parse_args()
    fake = Faker('zh-CN')

    for i in range(int(args.__getattribute__('生成数量'))):
        profile = fake.profile()
        manager = {
            '姓名': profile['name'],
            '性别': '女' if profile['sex'] == 'F' else '男',
            '身份证号码': profile['ssn'],
            '生日': profile['birthdate'].strftime('%Y-%m-%d'),
            '手机号': fake.phone_number(),
            '地址': profile['address'],
            '用户名': profile['username']
        }
        print(json.dumps(manager, indent=4, ensure_ascii=False))
        

if __name__ == "__main__":
    main()
