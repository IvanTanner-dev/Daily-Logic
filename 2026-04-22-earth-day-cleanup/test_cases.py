import solution

def test_get_cleanup_score():

      
    assert get_cleanup_score(["bottle", "straw", "shoe", "battery"]) == 44

    assert get_cleanup_score(["electronics", "straw", "newspaper", "bottle", "bag"]) == 58

    assert get_cleanup_score(["shoe", "can", "can", "can", "bottle", "bottle", "straw", "straw", "straw"]) == 79

    assert get_cleanup_score(["mattress", ["rare", 80], "tire", "tire", "tire", ["rare", 95]]) == 358

    assert get_cleanup_score(["bottle", "can", "can", "shoe", "shoe", ["rare", 56], "bottle", "bottle", "can", "can", "electronics", "bottle", ["rare", 48], "bottle", "can", "can", "can", "can", "can", "can", "can"]) == 383

if __name__ == "__main__":
    test_get_cleanup_score()