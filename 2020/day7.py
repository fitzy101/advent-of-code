import re
import textwrap

rule_r = r'(?P<parent_bag>\w+ \w+){1} bags contain (?P<child_bags>((\d) (\w+ \w+) (?:bag(?:s)?)(?:[,.]\s?))+|(no other bags)\.)'
bag_r = r'(\d) (\w+ \w+)'

def p1():
    input_file = "day7.input"
    with open(input_file) as f:
        rules = [rule for rule in f.read().split('\n') if rule != '']

    bag_rules = {}
    for rule in rules:
        match = re.match(rule_r, rule).groupdict()
        bag_rules[match['parent_bag']] = match['child_bags']

    def find_wanted_in_rules(bag_rules, wanted, seen):
        found_count = 0
        for parent, children in bag_rules.items():
            if wanted in children and parent not in seen:
                found_count += 1
                found_count += find_wanted_in_rules(bag_rules, parent, seen)
                seen.add(parent)
        return found_count
    print(find_wanted_in_rules(bag_rules, 'shiny gold', set()))


def p2():
    input_file = "day7.input"
    with open(input_file) as f:
        rules = [rule for rule in f.read().split('\n') if rule != '']

    bag_rules = {}
    for rule in rules:
        match = re.match(rule_r, rule).groupdict()
        child_bags = re.findall(bag_r, match['child_bags']) 
        bag_rules[match['parent_bag']] = [{'amount': int(r[0]), 'colour': r[1]} for r in child_bags]

    def find_bag_count(bags, wanted):
        return 1 + sum([child['amount'] * find_bag_count(bags, child['colour']) for child in bags[wanted]])

    print(find_bag_count(bag_rules, 'shiny gold') - 1)

if __name__ == '__main__':
    p1()
    p2()

