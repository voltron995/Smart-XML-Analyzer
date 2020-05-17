import os
import sys
from fuzzywuzzy import fuzz
from bs4 import BeautifulSoup

DEFAULT_TARGET_ID = "make-everything-ok-button"

def main():
    path_to_original_html, path_to_diff_html, target_element_id = handle_application_parameters()
    original_html = open(path_to_original_html).read()
    diff_html = open(path_to_diff_html).read()

    original_soup = BeautifulSoup(original_html, 'lxml')
    diff_soup = BeautifulSoup(diff_html, 'lxml')
    original_tag = original_soup.find(id=target_element_id)
    similar_tags = diff_soup.find_all(original_tag.name, {"class": 'btn'})
    original_attributes = extract_comperison_attributes(original_tag)

    similar_tag_attributes = dict()
    per_attr_similarity = dict()


    for tag in similar_tags:
        path = find_path(tag)
        key = path + " | " + str(id(tag))
        similar_tag_attributes[key] = extract_comperison_attributes(tag)

    for key, value in similar_tag_attributes.items():
        per_attr_similarity[key] = find_similarity_level(original_attributes, value)

    similar_tag, similarity_level = find_most_similiar_tag(per_attr_similarity)

    print("Original tag attribute values : {}".format(original_attributes))
    print("Path to the most similar tag in diff_case : {}".format(similar_tag.split('|')[0]))
    print("Tag attribute values : {}".format(similar_tag_attributes[similar_tag]))
    print("Similarity per tag attribute : {}".format(per_attr_similarity[similar_tag]))
    print("Final similarity score : {}".format(similarity_level))


def find_most_similiar_tag(common_tags):
    total_scores = dict()
    for key, value in common_tags.items():
        total_scores[key] = sum(value.values())/len(value.values()),
    max_key = max(total_scores, key=total_scores.get)
    return max_key, total_scores[max_key]


def find_similarity_level(attr_set1, attr_set2):
    similarity_levels = dict()
    for key, value in attr_set1.items():
        if key in attr_set2.keys():
            similarity_levels[key] = fuzz.token_sort_ratio(attr_set1[key], attr_set2[key])
    return similarity_levels

def find_path(current_tag):
    path_tags = [p.name for p in current_tag.parents][::-1]
    path_tags.append(current_tag.name)
    return " > ".join(path_tags)

def extract_comperison_attributes(tag):
    tag_attrs = dict()
    try:
        tag_attrs['class'] = " ".join(tag.attrs["class"])
    except KeyError:
        pass
    try:
        tag_attrs['title'] = tag.attrs["title"]
    except KeyError:
        pass
    try:
        tag_attrs['href'] = tag.attrs["href"]
    except KeyError:
        pass
    try:
        tag_attrs['text'] = tag.string.strip()
    except AttributeError:
        pass
    return tag_attrs

def handle_application_parameters():

    try:
        path_to_original_html = sys.argv[1]
    except IndexError:
        sys.exit("Please provide original file")
    try:
        path_to_diff_html = sys.argv[2]
    except IndexError:
        sys.exit("Please provide diff file")
    try:
        target_element_id = sys.argv[3]
    except IndexError:
        target_element_id = DEFAULT_TARGET_ID

    return path_to_original_html, path_to_diff_html, target_element_id


if __name__ == "__main__":
    main()
