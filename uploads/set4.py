setA={1,2,3,4,5}
setB={4,5,6,7,8}
def union_sets(setA,setB):
    union_result=setA.union(setB)
    print(f"union of seta and setb:{union_result}")
def intersection_sets(setA,setB):
    intersection_result=setA.intersection(setB)
    print(f"intersection of seta and setb:{intersection_result}")
def difference_sets(setA,setB):
    difference_result=setA.difference(setB)
    print(f"difference of seta and setb:{difference_result}")
def symmetric_difference_sets(setA,setB):
    symmetric_difference_result=setA.symmetric_difference(setB)
    print(f" symmetric_difference of seta and setb:{symmetric_difference_result}")
def subset_check(setA,setB):
    is_subset=setA.issubset(setB)
    print(f"Is seta subset of setb?:{is_subset}")
def superset_check(setA,setB):
    is_superset=setA.issuperset(setB)
    print(f"Is seta superset of setb?:{is_superset}")
def disjoint_check(setA,setB):
    is_disjoint=setA.isdisjoint(setB)
    print(f"Are seta and setb disjoint?:{is_disjoint}")
    
print(f"setA:{setA}")
print(f"setB:{setB}")

union_sets(setA,setB)
intersection_sets(setA,setB)
difference_sets(setA,setB)
symmetric_difference_sets(setA,setB)
subset_check(setA,setB)
superset_check(setA,setB)
disjoint_check(setA,setB)
