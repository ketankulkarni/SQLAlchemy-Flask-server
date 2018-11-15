import graphene

class Balance(graphene.ObjectType):
    principle = graphene.Int()
    interest = graphene.Int()

class BalanceInstance:
    principle=100
    interest=20

def resolve_getBalance(*_):
    return BalanceInstance()