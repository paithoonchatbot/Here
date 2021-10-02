import hashlib

text = ("e19ac44291e27bf7c3d8eea3758c7aeb899fc316")

for nonce in range (100000000):
	input = text+str(nonce)
	hash = hashlib.sha256(input.encode()).hexdigest()
	print(input,hash)
	if hash.startswith("0000"):
		print ("Found Hash")
		break