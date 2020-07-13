# pylint: disable=C0103


def verify_class_structure(klass):
    assert isinstance(klass, type)

    mro = klass.mro()
    assert len(mro) == 2
    assert mro == [klass, object]

    meth_add = getattr(klass, "add")
    meth_find = getattr(klass, "find")

    assert callable(meth_add), f"no method 'add' in {klass}"
    assert callable(meth_find), f"no method 'find' in {klass}"


def verify_class(klass):
    verify_class_structure(klass)


def verify_module(module, dataset):
    class_name = "ContactBook"
    assert hasattr(module, class_name)

    ContactBook = getattr(module, class_name)
    verify_class(ContactBook)

    obj = ContactBook()
    result = []

    for line in dataset[1:]:
        op, contact = line.split()
        if op == "add":
            obj.add(contact)
            continue
        if op == "find":
            n = obj.find(contact)
            result.append(n)

    assert result == [2, 0]


def test(modules_level06, dataset_contacts_short):
    for module in modules_level06.values():
        verify_module(module, dataset_contacts_short)
