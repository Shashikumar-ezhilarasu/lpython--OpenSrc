def _lpython_strcmp_eq(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    i: i32
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

def _lpython_strcmp_noteq(a: str, b: str) -> bool:
    return not _lpython_strcmp_eq(a, b)

def f():
    assert _lpython_strcmp_eq("a", "a")
    assert not _lpython_strcmp_eq("a2", "a")
    assert not _lpython_strcmp_eq("a", "a123")
    assert not _lpython_strcmp_eq("a23", "a24")
    assert _lpython_strcmp_eq("a24", "a24")
    assert _lpython_strcmp_eq("abcdefg", "abcdefg")
    assert not _lpython_strcmp_eq("abcdef3", "abcdefg")

    assert _lpython_strcmp_noteq("a2", "a")
    assert _lpython_strcmp_noteq("a", "a123")
    assert _lpython_strcmp_noteq("a23", "a24")
    assert _lpython_strcmp_noteq("abcdef3", "abcdefg")
    assert not _lpython_strcmp_noteq("a24", "a24")

f()
