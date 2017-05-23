op = {'RINA':'Region India', 'RMEA':'Region Middle East', 'RSSA':'Region Sub-Saharan Africa', 'RNEA':'Region North East Asia', 'RASO':'Region South East Asia & Oceania'}
region = 'RINA'
print("Region %s stands for %s"%(region,op.get(region,None)))
