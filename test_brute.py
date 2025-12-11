from brute import Brute

def describe_brute_functionality():
    def describe_init_functionality():
        def it_sets_the_correct_hash_target():
            brute = Brute("123")

            assert brute.target == "3c9909afec25354d551dae21590bb26e38d53f2173b8d3dc3eee4c047e7ab1c1eb8b85103e3be7ba613b31bb5c9c36214dc9f14a42fd7a2fdb84856bca5c44c2"
    def describe_brute_once_functionality():
        pass
    def describe_brute_many_functionality():
        pass