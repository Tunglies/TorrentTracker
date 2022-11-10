import re



with open("./trackers.txt") as tf:
    trackers = tf.read()

domains = re.findall("\/\/(.*)(?=:)", trackers)
deduplicate_domains = set(domains)

with open("./domains.txt", "w+") as df:
    df.write("\n".join(deduplicate_domains))