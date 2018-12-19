print("BUCK CONVERTER CACULATOR\n\n")

po=input("\nEnter max output power:")
fs=input("\nEnter switching frequency in HZ:")
vor=input("\nEnter output voltage ripple in mv:")

vi=input("\nEnter input voltage:")

vi=vi*1.0

vo=input("\nEnter output voltage:")

vo=vo*1.0

ilrp=input("\nEnter inductor ripple current(%of IL 0 -1):")

d=vo/vi
io=po/vo
ilr=io*ilrp
l=(vo/fs)*(1-d)/(ilr)
print("\nDuty={}".format(d))
print("\nOutput current={} A".format(io))
print("\nInductor ripple current={} A".format(ilr))
print("\nInductor in H={} H".format(l))
