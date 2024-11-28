from gooey import Gooey, GooeyParser

@Gooey()
def save_user():
    parser = GooeyParser(description="Saving data")
    parser.add_argument("username", help="Enter your username:")
    parser.add_argument("password", help="Enter your password:", widget="PasswordField")
    parser.add_argument("ID", help="Enter your ID:")
    args = parser.parse_args()

    found=False
    with open("users.txt", "r") as file:
        for line in file:
            username, password, ID = line.strip().split(",")
            if username == args.username and password == args.password and ID == args.ID:
                found=True
                break

    if found:
        print("The user has been found")
    else:
        print("The user has not been found")
save_user()
# در این برنامه باگ وجود داشت  و برای رفع اونا از هوش مصنوعی کمک گرفتم مثلا اینکه برنامه میومد کل اطلاعات قبلی را هم برسی و به همه آنها 
#  :جواب میداد که با استفاده از فاند=فالس و ترو رفع شد و همچنین برسی اطلاعات داده شده به صورت خطی و با در نظر گرفتن کاما ها(جدا جدا) 
#         for line in file:
        #    username, password, ID = line.strip().split(",")
# که دقیق متوجه نشدم چطور کار میکنن اگر شد تو کلاس یا هر جا صلاح میدونین توضیح کوتاهی بدین ممنون میشم
