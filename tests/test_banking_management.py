from unittest.mock import patch
from service.user_valid import UserValid
from model.db_methods import DbMethods
from view.create_acount import create_account

def test_check_name(): 
    assert UserValid.check_name("ananya")
    assert not UserValid.check_name(" ")
    assert not UserValid.check_name(1099)
    assert not UserValid.check_name("ananya12@")
    assert not UserValid.check_name("ananya12")

def test_check_balance(): 
    assert UserValid.check_balance(6000)
    assert not UserValid.check_balance(10)
    assert not UserValid.check_balance("ananya12")

def test_check_mail(): 
    assert not UserValid.check_mail(6000)
    assert not UserValid.check_mail("10")
    assert not UserValid.check_mail("ananya12")
    assert not UserValid.check_mail("ananya12@yash")
    assert not UserValid.check_mail("ananya12@yash")

def test_check_password(): 
    assert UserValid.check_password("aA1!q1q1q1q1q1")
    assert UserValid.check_password("swsswwaA !1q1q1q1")
    assert not UserValid.check_password(10)
    assert not UserValid.check_password("ananya12")
    assert not UserValid.check_password("aa12!")
    assert not UserValid.check_password("aAa12!")
    assert not UserValid.check_password("")


# def test_create_account():
#     db = DbMethods()
#     assert db.create_account(1734, "ananya joshiji", "aj@yash.com", "aA1!q1q1q1q1", 1000)
    # assert not db.create_account(1134, "ananya ", "aj@yash.com", "aA1!q1q1q1q1", 1000)

def test_login():
    db = DbMethods()
    assert db.login("joshi@yash.com", "aA1!q1q1q1q1q1")
    assert not db.login("joshi@yash.com", "aA1!q1q1q11")
    assert not db.login("josh2ewi@yash.com", "q1q1q1q1q1!q1q1q11")

def test_cr_amount():
    db = DbMethods()
    assert db.cr_amount("joshi@yash.com", 100)
    assert not db.cr_amount("joshq1i@yash.com", 1200)
    assert not db.cr_amount("joshi@yash.com", "sdvff")

def test_debit_money():

    db = DbMethods()
    assert db.debit_money("joshi@yash.com", 180)
    assert not db.debit_money("joshisgh1@yash.com", 180)

@patch('builtins.input', side_effect=["ananya", "ajoshi@yash.com", "aA1!q1q1q1q1q1", 2000])  
def test_create_account_controller(mock_input):
    ob = create_account()
    assert ob.run(  )
