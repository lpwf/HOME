def instances_counter(cls):
    class NewClass(cls):
        instances_count = 0

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            NewClass.instances_count += 1

        @classmethod
        def get_created_instances(cls):
            return cls.instances_count

        @classmethod
        def reset_instances_counter(cls):
            count = cls.instances_count
            cls.instances_count = 0
            return count

    return NewClass


@instances_counter
class User:
    pass


if __name__ == '__main__':
    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
