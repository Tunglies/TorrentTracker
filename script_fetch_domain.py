import re



with open("./trackers.txt") as tf:
    trackers = tf.read()

domains = re.findall("\/\/(.*)(?=:)", trackers)
deduplicate_domains = set(domains)
without_number_address = list(filter(lambda x: not all(map(lambda y: y.isdigit(), x.split("."))), deduplicate_domains))

with open("./domains.txt", "w+") as df:
    df.write("\n".join(without_number_address))