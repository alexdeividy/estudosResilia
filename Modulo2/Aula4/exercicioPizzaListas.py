#Lista original de pizzas
pizzas = ["Calabresa", "Mussarela", "Marguerita"]

#Clonando a lista original
friend_pizzas = pizzas[:]

#Adicionado Escarola com o metodo append
friend_pizzas.append("Escarola")

#Adicionado Portuguesa com o metodo insert
friend_pizzas.insert(2,"Portuguesa")

print("As minhas pizzas favoritas sao:",pizzas)
print("As pizzas favoritas do meu amigo sao:",friend_pizzas)