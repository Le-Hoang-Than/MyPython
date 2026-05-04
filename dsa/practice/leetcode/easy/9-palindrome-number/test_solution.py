from solution import Solution


def test_palindrome_even_digits():
    s = Solution()

    assert s.isPalindrome(1221) is True


def test_palindrome_odd_digits():
    s = Solution()
    assert s.isPalindrome(121) is True


def test_negative_number():
    s = Solution()

    assert s.isPalindrome(-121) is False


def test_palindrome_false():
    s = Solution()
    assert s.isPalindrome(1231) is False


def test_palindrome_last_zero():
    s = Solution()
    assert s.isPalindrome(10) is False


def test_palindrome_single_digit():
    s = Solution()
    assert s.isPalindrome(1) is True
