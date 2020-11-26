class Checker:
    def __init__(self, code, symbols=[]):
        self.code = code
        self.symbols = symbols




    def fillSymbols(self):
        self.symbols = []
        for thing in self.code.split("------------------------------------------------------------------------------"):
            thing = thing.replace("-----", "").replace("--", "")
            # print(thing)
            dashes = 3
            i=0
            tempStr = ""
            for part in thing:
                # print(part)
                if dashes == 3 and i < 4:
                    tempStr += part
                    i += 1
                if i >= 4:
                    dashes = 0
                    self.symbols.append(tempStr)
                    i=0
                    tempStr = ""
                if part == '-':
                    dashes += 1

    def getSymbolDuplicates(self):
        duplicates = []
        output = []
        for i in range(len(self.symbols)):
            for n in range(len(self.symbols)):
                if i != n and self.symbols[i] == self.symbols[n] and self.symbols[i] not in duplicates:
                    duplicates.append(self.symbols[i])
                    print("Found duplicate of symbols: %s" % (self.symbols[i]), "at index: %d and %d" % (i+1, n+1))
                    outputStr = "Found duplicate of symbols: %s at index: %d and %d" % (self.symbols[i], i+1, n+1)
                    output.append(outputStr)
        return output

    def getCharachterDuplicates(self):
        m = 1
        output = []
        for symbol in self.symbols:
            duplicates = []
            for i in range(len(symbol)):
                for n in range(len(symbol)):
                    if n != i and symbol[i] == symbol[n] and symbol[n] not in duplicates:
                        duplicates.append(symbol[n])
                        print("Found duplicates of characters at %d" % m)
                        output.append("Found duplicates of characters at %d" % m)
            m+=1
        return output


if __name__ == "__main__":
    test1 = Checker("""
    qasw-sol-1-rmdh-sol-2-kjfh-sol-3-cvdf-sol-4-kdhg-sol-5-thfg-sol-6-qsty-sol-7------------------------------------------------------------------------------vbfg-sol-8-uhfg-sol-9-bvgf-sol-10-pokj-sol-11-fhvb-sol-12-tcnf-sol-13-------------------------------------------------------------------------------------qncg-sol-14-vcbf-sol-15-skjf-sol-16-tmsk-sol-17-jhbn-sol-18-sfdv-sol-19-----------------------------------------------------------------------------------trfg-sol-20-cbvf-sol-21-hnbv-sol-22-fxvc-sol-23-zkfh-sol-24-idfb-sol-25-----------------------------------------------------------------------------------rhgf-sol-26-bfhg-sol-27-rhgf-sol-28-jmnh-sol-29-plkj-sol-30-nbfg-sol-31-----------------------------------------------------------------------------------olkj-sol-32-cxsd-sol-33-thsd-sol-34-redf-sol-35-hgfy-sol-36-wsde-sol-37-----------------------------------------------------------------------------------vcdf-sol-38-nbvc-sol-39-zjdh-sol-40-ukjh-sol-41-rjgm-sol-42-xcfd-sol-43-----------------------------------------------------------------------------------eudj-sol-44-qaif-sol-45-fmjg-sol-46-utnd-sol-47-mnsj-sol-48-yfhg-sol-49-----------------------------------------------------------------------------------kmnb-sol-50-xkjf-sol-51-tedg-sol-52-ofdn-sol-53-asdf-sol-54-uytr-sol-55-----------------------------------------------------------------------------------mnbv-sol-56-sdfg-sol-57-tyui-sol-58-ghjk-sol-59-erty-sol-60-dfgh-sol-61-----------------------------------------------------------------------------------mnas-sol-62-fghj-sol-63-nbcv-sol-64-jmnh-sol-65-cvhg-sol-66-rebv-sol-67-----------------------------------------------------------------------------------rytu-sol-68-vbgj-sol-69-zaxs-sol-70-cdvf-sol-71-nhmj-sol-72-defr-sol-73-----------------------------------------------------------------------------------zacd-sol-74-rdik-sol-75-nfkh-sol-76-zapo-sol-77-xfbh-sol-78-rinb-sol-79-----------------------------------------------------------------------------------rvcn-sol-80-ioty-sol-81-emng-sol-82-cyhg-sol-83-akhf-sol-84-uinb-sol-85-----------------------------------------------------------------------------------kdjf-sol-86-jsad-sol-87-oiza-sol-88-snfy-sol-89-rmdh-sol-90-prmm-sol-91-----------------------------------------------------------------------------------

    """)

    test1.getSymbolDuplicates()
    test1.getCharachterDuplicates()
