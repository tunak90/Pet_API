from api import Pets

pt = Pets()


# @pytest.mark.parametrize('email', 'expected_result',
#                          [(settings.VALID_EMAIL, 200),
#                           (settings.INVALID_EMAIL, 400),
#                           ])
# def test_get_token(email, expected_result):
def test_get_token():
    results = pt.get_token()
    status = results[1]
    token = results[0]
    assert token
    assert status == 200
    # assert status == expected_result


def test_get_list_users():
    status = pt.get_list_users()[0]
    my_id = pt.get_list_users()[1]
    assert status == 200
    assert my_id


def test_create_pet():
    status = pt.create_pet()[1]
    pet_id = pt.create_pet()[0]
    assert status == 200
    assert pet_id


def test_upload_pet_photo():
    status = pt.upload_pet_photo()[0]
    link = pt.upload_pet_photo()[1]
    assert status == 200
    assert link


def test_add_like_pet():
    status = pt.add_like_pet()
    assert status == 200


def test_add_comment_pet():
    status = pt.add_comment_pet()[0]
    comment_id = pt.add_comment_pet()[1]
    assert status == 200
    assert comment_id


def test_get_pets_list():
    status = pt.get_pets_list()[1]
    list_of_pets = pt.get_pets_list()[0]
    assert status == 200
    assert list_of_pets


def test_get_pet_by_id():
    status = pt.get_pet_by_id()[0]
    pet_id_return = pt.create_pet()[1]
    assert status == 200
    assert pet_id_return


def test_delete_pet_by_id():
    status = pt.delete_pet_by_id()
    assert status == 200


def test_update_pet():
    status = pt.update_pet()[0]
    pet_id_return = pt.update_pet()[1]
    assert status == 200
    assert pet_id_return
