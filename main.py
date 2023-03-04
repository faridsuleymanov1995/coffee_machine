MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    'money': 0
}

def check_sorce( menu, resurces):
    '''return enough resources or not'''
    for i in menu['ingredients']:
        if menu['ingredients'][i] > resurces[i]:
            print(f'sorry don\'t enauogh {i} ')
            return False
    return True

def new_recorus(menu,resurces):
    '''it adds machine new recourses'''
    for i in menu['ingredients']:
        x = resurces[i] - menu['ingredients'][i]
        resurces[i] = x
    b = resurces['money'] + menu['cost']
    resurces['money'] = b
    return resurces

def money_change(menu, money):
    '''it returns enough money if it has then return exchange'''
    if menu['cost'] > money:
        print(f'sorry you don\'t have enough money')
        return 'no'
    return money - menu['cost']

def user_mone():
    '''calculate coins and returns'''
    quartes = int(input('how much quarter: '))
    dimes = int(input('how much dimes: '))
    nickles = int(input('how much nickles: '))
    pennies = int(input('how much pennies: '))
    money = 0.25 * quartes + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return money


insert = 'on'
while not insert == 'off':
    insert = input('What would you like? (espresso/latte/cappuccino): ')
    if insert == 'report':
        for i in resources:
            if i == 'coffee':
                print(f'{i} : {resources[i]}g')
            elif i == 'money':
                print(f'{i} : ${resources[i]}')
            else:
                print(f'{i} : {resources[i]}l')
    else:
        if insert in ['espresso', 'latte', 'cappuccino']:

            check = check_sorce(MENU[insert],resources)
            if check:
                money = user_mone()
                money1 = money_change(MENU[insert], money)
                if money1 != 'no':
                    user_money = round(money1, 2)
                    resources = new_recorus(MENU[insert], resources)
                    print(f'here you {insert} ☕ and your exchange ${user_money}')


