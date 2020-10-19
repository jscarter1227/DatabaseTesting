from pprint import pprint

people = [
    {"name": "Alex Groce",
           "occupation": "prof",
           "favorite color" : "fuligin"},
    {"name": "Ghengis Khan",
           "occupation": "warlord",
           "favorite color" : "blood of his foes"},
    {"name": "Marie Curie",
           "occupation": "scientist",
           "favorite color" : "radium green"}]
    

def rel_select(predicate, relation):
    new_relation = []
    for tuple in relation:
        if predicate(tuple):
            new_relation.append(tuple)

    return new_relation

def rel_project(attributes, relation):
    new_relation = []
    for tuple in relation:
        new_tuple={}
        for field in tuple:
            if field in attributes:
                new_tuple[field] = tuple[field]
        new_relation.append(new_tuple)
    return new_relation

def rel_rename(new_names, relation):
    new_relation = []
    for tuple in relation:
        new_tuple={}
        for field in tuple:
            changed = False;
            for (old_name, new_name) in new_names:
                if field == old_name:
                    new_tuple[new_name] = tuple[field]
                    changed = True
            if not changed:
                new_tuple[field] = tuple[field]
        new_relation.append(new_tuple)
    return new_relation

def union_compatible(relation1, relation2):
    return ((len(relation1) == 0) or (len(relation2) == 0) or
    (len(relation1[0].keys()) == len(relation2[0].keys())))

def rel_union(relation1, relation2):
    if not union_compatible(relation1, relation2):
        raise TypeError
    return relation1 + relation2 

def rel_intersect(relation1, relation2):
    new_relation = []
    for tuple in relation1:
        if tuple in relation2:
            new_relation.append(tuple)
    return new_relation

def rel_minus(relation1, relation2):
    new_relation = []
    for tuple in relation1:
        if tuple not in relation2:
            new_relation.append(tuple)
    return new_relation

def not_likes_green(tuple):
    return not("green" in tuple["favorite color"])

#pprint.pprint(rel_rename([("name", "moniker")],
#                       rel_project(["name"],
#              rel_select(not_likes_green, people))))

#SELECT name FROM People WHERE they dont like green


no_green = rel_select(not_likes_green, people)
green = rel_minus(people, no_green)
everybody = rel_union(no_green, green)
nobody = rel_intersect(no_green, green)

pprint(no_green)
pprint(green)
pprint(everybody)
pprint(nobody)

    
