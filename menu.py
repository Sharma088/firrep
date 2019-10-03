class Menu(object):
    def __init__(self):
        self.user=input("Enter your author name")
        self.user_blog=None
        if self._user_has_account():
            print("welcome back{}".format(self.user))
        else:
            self._prompt_user_for_account()
    def _user_has_account(self):
        blog=Database.find_one('blogs',{author:self.user})
        if blog is not None:
            self.user_blog=blog
            return True
        else:
            return False
    def _prompt_user_for_account(self):
        title=input("Enter blog title:")
        description=input("Enter blog description")
        blog=Blog(author=self.user,
        title=title,
        description=description)
        blog.save_to_mongo()
        self.user_blog=blog
    def run_menu(self):
        read_or_write=input("Do you want to red(R) or write(W) blogs?")
        if read_or_write=='R'

