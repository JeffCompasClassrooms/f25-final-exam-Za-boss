from christmas_list import ChristmasList
import os


def describe_test_christmas_list():
    def describe_constructor():
        def it_creates_a_new_file_if_file_does_not_exist():
            a_list = ChristmasList("my_list.pkl")

            assert os.path.isfile("my_list.pkl")

            os.remove("my_list.pkl")        
        def it_saves_an_empty_array_if_file_does_not_exist():
            a_list = ChristmasList("my_list.pkl")

            assert a_list.loadItems() == []

            os.remove("my_list.pkl")
        def it_assigns_filename_on_init():
            a_list = ChristmasList("my_list.pkl")

            assert a_list.fname == "my_list.pkl"

            os.remove("my_list.pkl")
    def describe_loading():
        def it_loads_correctly_when_list_is_empty():
            a_list = ChristmasList("my_list.pkl")

            assert a_list.loadItems() == []

            os.remove("my_list.pkl")
        def it_loads_correctly_when_there_are_two_handles_to_same_list():
            a_list = ChristmasList("my_list.pkl")
            b_list = ChristmasList("my_list.pkl")
            
            assert a_list.loadItems() == []
            assert b_list.loadItems() == []

            os.remove("my_list.pkl")
        def it_loads_correctly_when_there_is_content():
            a_list = ChristmasList("my_list.pkl")

            a_list.saveItems(["a" * 500])

            assert a_list.loadItems() == ["a" * 500]

            os.remove("my_list.pkl")
        def it_loads_large_amounts_of_content_successfully():
            a_list = ChristmasList("my_list.pkl")

            a_list.saveItems(["ab" * 50000])

            assert a_list.loadItems() == ["ab" * 50000]

            os.remove("my_list.pkl")
        def it_correctly_loads_non_array_items():
            #This is just to verify that it can, if you actually do this it will break things
            a_list = ChristmasList("my_list.pkl")

            a_list.saveItems("b")

            assert a_list.loadItems() == "b"

            os.remove("my_list.pkl")
    def describe_saving():
        def it_correctly_saves_a_single_item():
            a_list = ChristmasList("my_list.pkl")

            a_list.saveItems(["hello"])

            assert a_list.loadItems() == ["hello"]
            os.remove("my_list.pkl")
        
        def two_handles_can_write_to_same_list():
            a_list = ChristmasList("my_list.pkl")
            b_list = ChristmasList("my_list.pkl")

            a_list.saveItems(["bike", "car"])
            b_list.saveItems(["house", "garage"])

            assert a_list.loadItems() == ["house", "garage"]
            assert b_list.loadItems() == ["house", "garage"]
            os.remove("my_list.pkl")
        def previous_content_gets_overwritten():
            a_list = ChristmasList("my_list.pkl")

            a_list.saveItems(["bike"])
            a_list.saveItems(["Not bike"])

            assert a_list.loadItems() == ["Not bike"]

            os.remove("my_list.pkl")
        def saving_empty_content_works():
            a_list = ChristmasList("my_list.pkl")

            a_list.saveItems([])

            assert a_list.loadItems() == []

            os.remove("my_list.pkl")
    def describe_adding():
        def it_correctly_adds_to_empty_list():
            a_list = ChristmasList("my_list.pkl")

            a_list.add("Puppy")

            assert a_list.loadItems() == [{"name": "Puppy", "purchased": False}]

            os.remove("my_list.pkl")
        def it_adds_a_new_item_to_the_list():
            a_list = ChristmasList("my_list.pkl")

            a_list.add("Puppy")

            assert a_list.loadItems() == [{"name": "Puppy", "purchased": False}]

            os.remove("my_list.pkl")
        def it_marks_the_item_as_not_purchased_when_added():
            a_list = ChristmasList("my_list.pkl")

            a_list.add("Puppy")

            assert a_list.loadItems()[0]['purchased'] == False

            os.remove("my_list.pkl")
        def two_handles_can_add_to_same_list():
            a_list = ChristmasList("my_list.pkl")
            b_list = ChristmasList("my_list.pkl")

            a_list.add("Puppy")
            b_list.add("Kitten")

            assert a_list.loadItems() == [{"name": "Puppy", "purchased": False}, {"name": "Kitten", "purchased": False}]
            assert b_list.loadItems() == [{"name": "Puppy", "purchased": False}, {"name": "Kitten", "purchased": False}]

            os.remove("my_list.pkl")                                    
    def describe_check_off():
        def it_does_not_break_when_it_cant_find_the_item():
            a_list = ChristmasList("my_list.pkl")

            a_list.check_off("NULL")

            os.remove("my_list.pkl")
        def it_successfully_marks_the_item_as_purchased():
            a_list = ChristmasList("my_list.pkl")

            a_list.add("NULL")
            a_list.check_off("NULL")

            assert a_list.loadItems()[0]["purchased"] == True

            os.remove("my_list.pkl")            
    def describe_remove():
        def it_does_not_break_when_the_list_is_empty():
            a_list = ChristmasList("my_list.pkl")

            a_list.remove("NULL")

            os.remove("my_list.pkl")
        def it_does_not_break_when_it_cant_find_the_item():
            a_list = ChristmasList("my_list.pkl")

            a_list.add("nil")
            a_list.remove("NULL")

            os.remove("my_list.pkl")
        def it_successfully_removes_the_item():
            a_list = ChristmasList("my_list.pkl")

            a_list.add("nil")
            a_list.remove("nil")

            assert a_list.loadItems() == []

            os.remove("my_list.pkl")                                    
    def describe_print_list():
        def it_prints_blank_when_the_list_is_empty(capsys):
            a_list = ChristmasList("my_list.pkl")

            a_list.print_list()

            captured = capsys.readouterr()
            assert captured.out == ""

            os.remove("my_list.pkl")
        def it_prints_not_purchased_items_correctly(capsys):
            a_list = ChristmasList("my_list.pkl")

            a_list.add("dog")
            a_list.print_list()

            captured = capsys.readouterr()
            assert "[_] dog" in captured.out 

            os.remove("my_list.pkl")
        def it_prints_purchased_items_correctly(capsys):
            a_list = ChristmasList("my_list.pkl")

            a_list.add("dog")
            a_list.check_off("dog")
            a_list.print_list()

            captured = capsys.readouterr()
            assert "[x] dog" in captured.out 

            os.remove("my_list.pkl")
        def it_prints_a_complete_list_correctly(capsys):
            a_list = ChristmasList("my_list.pkl")

            a_list.add("dog")
            a_list.add("cat")
            a_list.add("skateboard")
            a_list.add("fish")
            a_list.check_off("dog")
            a_list.print_list()

            captured = capsys.readouterr()
            assert ( 
            "[x] dog" in captured.out 
            and "[_] cat" in captured.out
            and "[_] skateboard" in captured.out
            and "[_] fish" in captured.out
            )
            os.remove("my_list.pkl")                        