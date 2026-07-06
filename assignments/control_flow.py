# Problem Statement:

# A data analyst is building a Python utility to process and analyze tag data scraped from a content platform. Tags arrive as messy raw lists that may contain duplicates and mixed types. The analyst needs a script that performs four tasks:

# Cleans a raw tag list by converting it to a set to remove duplicates, then reports the count of unique tags.
# Checks whether each of a set of "required tags" is a subset of the cleaned tag set using issubset().
# Creates a frozenset from the cleaned tag set and confirms it is hashable by calling hash() on it (catching the case where hashing fails with a clear message).
# Demonstrates the remove vs discard difference: attempts remove on a tag not in the set (catching the KeyError), then attempts discard on the same missing tag and confirms no error is raised.
# Constraints & Requirements:

# Use only Python built-ins — no third-party libraries.
# Implement all four tasks as separate functions: clean_tags, check_required_subset, make_frozen_hashable, and demo_remove_vs_discard.
# Handle expected errors (KeyError, TypeError) with try/except and print descriptive messages.
# Do not assume the raw tag list is pre-cleaned.
# Inlined Sample Data & Inputs:

# # Raw tag list (contains duplicates and mixed hashable types)
raw_tags = ["python", "data", "python", "ml", "data", "ai", "python", (1, 2), (1, 2), "ml"]

# # Required tags to check subset membership
required_tags_1 = {"python", "data"}   # both present — should be a subset
required_tags_2 = {"python", "java"}   # "java" is absent — NOT a subset
# Expected output for the sample above:
# Unique tag count: 5
# required_tags_1 is a subset: True
# required_tags_2 is a subset: False
# frozenset hash: <some integer>
# KeyError caught: 'java' is not in the set
# discard('java') completed without error



def clean_tags(raw_tags):
   cleaned_set=set(raw_tags)
   count=0
   for value in cleaned_set:
       count=count+1
   print('Unique tag count : ',count)
   return cleaned_set
   

def check_required_subset(cleaned:set, required:set):
    isSubset=required.issubset(cleaned)
    if(isSubset):
        print(f"{required} is a subset of {cleaned}: {isSubset}")
    else:
        print(f"{required} is not a subset of {cleaned}: {isSubset}")
    return isSubset

def make_frozen_hashable(cleaned:set):
    frozen_cleaned:frozenset=frozenset(cleaned)
    try :
        print(frozen_cleaned.__hash__())
    except TypeError as e:
        print(f"Error is {e}")    
    pass

# difference between discard and remove is that discard will not throw an error if the element is not present in the set, while remove will throw a KeyError.
def demo_remove_vs_discard(cleaned, missing_tag):
    try:
        cleaned.remove(missing_tag)
    except KeyError as e:
        print(f"KeyError caught: {e}")
    try:
        cleaned.discard(missing_tag)
        print(f"discard('{missing_tag}') completed without error")
    except Exception as e:
        print(f"Unexpected error during discard: {e}")


cleaned=clean_tags(raw_tags=raw_tags)
check_required_subset(cleaned=cleaned, required=required_tags_2)
make_frozen_hashable(cleaned=cleaned)
demo_remove_vs_discard(cleaned=cleaned, missing_tag='java')


