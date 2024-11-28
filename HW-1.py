from gooey import Gooey, GooeyParser

@Gooey()
def save_user():
    parser = GooeyParser(description="Saving data")
    parser.add_argument("username", help="Enter your username:")
    parser.add_argument("password", help="Enter your password:", widget="PasswordField")
    parser.add_argument("ID", help="Enter your ID:")
    args = parser.parse_args()

    with open("users.txt", "a") as file:
        file.write(f"{args.username},{args.password},{args.ID}\n")

    print("Datas have been saved successfully")

save_user()
