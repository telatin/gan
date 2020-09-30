# API Documentation: DSMZ PNU

Website: https://bacdive.dsmz.de/api/pnu/api-docs/

## Name: species

Query: https://bacdive.dsmz.de:443/api/pnu/name/Escherichia/coli/

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/776057/",
      "pnu_no": 776057,
      "label": "Escherichia coli",
      "species": "Escherichia coli",
      "species_epithet": "coli",
      "subspecies_epithet": null,
      "genus": "Escherichia",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "(Migula 1895) Castellani and Chalmers 1919",
      "taxon": "comb. nov. (AL)",
      "reference": "Int. J. Syst. Bacteriol. 30:225",
      "comment": null,
      "lpsn": "http://www.bacterio.net/escherichia.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-30083.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Castellani, A., Chalmers, A. J., (1919). Type genus: Bacteroides. In <i> Manual of tropical medicine </i>, pp. 959-960. Williams, Wood and Co.."
        },
        {
          "pubmed": null,
          "reference": "Migula, W., (1895). Bacteriaceae (Stäbchenbacterien). In <i> Die Natürlichen Pflanzenfamilien. Teil I, Abteilung Ia </i>, pp. 20-30. Edited by A. Engler, W. Engelmann."
        },
        {
          "pubmed": null,
          "reference": "Bergey, D. H., Buchanan, R. E., Gibbons, N. E., (1974). Bergey's manual of determinative Bacteriology. 8th. EditionEdited by R. E. Buchanan, The Williams & Wilkins Co.."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "ATCC 11775",
        "CCM 5172",
        "CIP 54.8",
        "DSM 30083",
        "NCDO 1989",
        "NCTC 9001",
        "CCUG 24",
        "CCUG 29300",
        "DSMZ 30083",
        "JCM 1649",
        "LMG 2092",
        "NBRC 102203",
        "NCCB 54008",
        "NCTC 9001."
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Escherichia+coli"
    }
  ]
}
```

## Species


- Filters: contains=, startswith=, endswith=, exclude=
- Example: https://bacdive.dsmz.de:443/api/pnu/species/?contains=entero&endswith=monas&exclude=coccus

```json
{
  "count": 134,
  "next": "https://bacdive.dsmz.de/api/pnu/species/?exclude=coccus&endswith=monas&contains=entero&page=2",
  "previous": null,
  "results": [
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/772898/",
      "pnu_no": 772898,
      "label": "Aeromonas enteropelogenes",
      "species": "Aeromonas enteropelogenes",
      "species_epithet": "enteropelogenes",
      "subspecies_epithet": null,
      "genus": "Aeromonas",
      "familia": "Aeromonadaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Schubert et al. 1991",
      "taxon": "sp. nov. (VL)",
      "reference": "Int. J. Syst. Bacteriol. 41:456",
      "comment": null,
      "lpsn": "http://www.bacterio.net/aeromonas.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-6394.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Schubert, R. H. W., Hegazi, M., Wahlig, W. (1990). <i>Aeromonas enteropelogenes</i> species nova. <i> Hyg.Med. </i><b> 15 </b>: 471-472 ."
        },
        {
          "pubmed": null,
          "reference": "(1991). Validation of the publication of new names and new combinations previously effectively published outside the IJSB. List No. 38. <i> Int.J.Syst.Bacteriol. </i><b> 41 </b>: 456-457 ."
        }
      ],
      "correct_name": null,
      "synonyms": [
        {
          "synonym_type": "heterotypic syn.",
          "synonym": "<i>Aeromonas</i> <i>trota</i> "
        },
        {
          "synonym_type": "orthographically incorrect name",
          "synonym": "\"<i>Aeromonas tructi</i>\" "
        },
        {
          "synonym_type": "orthographically incorrect name, heterotypic syn.",
          "synonym": "<i>Chakrabarty</i> <i>trota</i> "
        }
      ],
      "type_strain": [
        "DSM 6394",
        "J11",
        "ATCC 49803",
        "CECT 4487",
        "CIP 104434",
        "JCM 8355",
        "LMG 12646"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Aeromonas+enteropelogenes"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775928/",
      "pnu_no": 775928,
      "label": "Enterobacter aerogenes",
      "species": "Enterobacter aerogenes",
      "species_epithet": "aerogenes",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Hormaeche and Edwards 1960",
      "taxon": "species (AL)",
      "reference": "Int. J. Syst. Bacteriol. 30:225",
      "comment": "[DSMZ] homotypic synonym: Klebsiella mobilis",
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-30053.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Hormaeche, E., Edwards, P. R. (1960). A proposed genus <i>Enterobacter</i>. <i> Int.Bull.Bacteriol.Nomencl.Taxon. </i><b> 10 </b>: 71-74 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/777146/",
        "Klebsiella aerogenes"
      ],
      "synonyms": [
        {
          "synonym_type": "illegitimate name",
          "synonym": "<i>Klebsiella</i> <i>mobilis</i> "
        }
      ],
      "type_strain": [
        "ATCC 13048",
        "CDC 819-56",
        "DSM 30053",
        "NCTC 10006",
        "CCUG 1429",
        "CIP 60.86",
        "DSMZ 30053",
        "HAMBI 101",
        "HAMBI 1898",
        "IFO 13534",
        "JCM 1235",
        "LMG 2094",
        "NBRC 13534",
        "NCAIM B.01467"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Klebsiella+aerogenes"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775929/",
      "pnu_no": 775929,
      "label": "Enterobacter agglomerans",
      "species": "Enterobacter agglomerans",
      "species_epithet": "agglomerans",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "(Beijerinck 1888) Ewing and Fife 1972 emend. Beji et al. 1988",
      "taxon": "comb. nov. (VP)",
      "reference": "Int. J. Syst. Bacteriol. 38:77*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-3493.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Beji, A., Mergaert, J., Gavini, F., Izard, D., Kersters, K., Leclerc, H., DeLey, J. (1988). Subjective synonymy of <i>Erwinia herbicola, Erwinia milletiae</i> and <i>Enterobacter agglomerans</i> and redefinition of the taxon by genotypic and phenotypic data. <i> Int.J.Syst.Bacteriol. </i><b> 38 </b>: 77-88 ."
        },
        {
          "pubmed": null,
          "reference": "Ewing, W. H., Five, M. A. (1972). <i>Enterobacter agglomerans</i> (Beijerinck) comb. nov. (the herbicola-lathyri bacteria). <i> Int.J.Syst.Bacteriol. </i><b> 22 </b>: 4-11 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/779135/",
        "Pantoea agglomerans"
      ],
      "synonyms": [
        {
          "synonym_type": "heterotypic syn.",
          "synonym": "<i>Erwinia</i> <i>herbicola</i> "
        },
        {
          "synonym_type": "heterotypic syn.",
          "synonym": "<i>Erwinia</i> <i>milletiae</i> "
        }
      ],
      "type_strain": [
        "ATCC 27155",
        "CIP 57.51",
        "DSM 3493",
        "NCTC 9381",
        "CCUG 539",
        "CDC 1461-67",
        "CFBP 3845",
        "DSMZ 3493",
        "ICMP 12534",
        "ICPB 3435",
        "JCM 1236",
        "LMG 1286",
        "NBRC 102470",
        "strain ATCC 27155"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Pantoea+agglomerans"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775930/",
      "pnu_no": 775930,
      "label": "Enterobacter amnigenus",
      "species": "Enterobacter amnigenus",
      "species_epithet": "amnigenus",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Izard et al. 1981",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Bacteriol. 31:35*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-4486.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Izard, D., Gavini, F., Trinel, P. A., Leclerc, H. (1981). Deoxyribunucleic acid relateness between <i>Enterobacter cloacae</i> and <i>Enterbacter amnigenus</i> sp.nov. <i> Int.J.Syst.Bacteriol. </i><b> 31 </b>: 35-42 ."
        },
        {
          "pubmed": null,
          "reference": "Izard, D., Gavini, F., Trinel, P. A., Leclerc, H. (1981). Deoxyribonucleic acid relatedness between <i>Enterobacter cloacae</i> and <i>Enterobacter amnigenus</i> sp. nov. <i> Int.J.Syst.Bacteriol. </i><b> 31 </b>: 37-42 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/791220/",
        "Lelliottia amnigena"
      ],
      "synonyms": null,
      "type_strain": [
        "ATCC 33072",
        "CUETM 77-118",
        "DSM 4486",
        "CCUG 14182",
        "CIP 103169",
        "DSMZ 4486",
        "HAMBI 1297",
        "JCM 1237",
        "LMG 2784",
        "NCTC 12124"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Lelliottia+amnigena"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775931/",
      "pnu_no": 775931,
      "label": "Enterobacter asburiae",
      "species": "Enterobacter asburiae",
      "species_epithet": "asburiae",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Brenner et al. 1988 emend. Hoffmann et al. 2005",
      "taxon": "sp. nov. (VL)",
      "reference": "Int. J. Syst. Bacteriol. 38:220",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-17506.html",
      "literature": [
        {
          "pubmed": "16014457",
          "reference": "(2005). Notification of changes in taxonomic opinion previously published outside the IJSEM. No. 2. <i> Int.J.Syst.Evol.Microbiol. </i><b> 55 </b>: 1403-1404 ."
        },
        {
          "pubmed": "15900966",
          "reference": "Hoffmann, H., Stindl, S., Ludwig, W., Stumpf, A., Mehlen, A., Heesemann, J., Monget, D., Schleifer, K. H., Roggenkamp, A. (2005). Reassignment of <i>Enterobacter dissolvens</i> to <i>Enterobacter cloacae</i> as <i>E. cloacae</i> subspecies <i>dissolvens</i> comb. nov. and emended description of <i> Enterobacter asburiae</i> and <i>Enterobacter kobei.</i>. <i> Syst.Appl.Microbiol. </i><b> 28 </b>: 196-205 ."
        },
        {
          "pubmed": "3711302",
          "reference": "Brenner, D. J., McWhorter, A. C., Kai, A., Steigerwalt, A. G., Farmer, J. J. (1986). <i>Enterobacter asburiae</i> sp. nov., a new species found in clinical specimens, and reassignement of <i>Erwinia dissolvens</i> and <i>Erwinia nimipressuralis</i> to the genus <i>Enterobacter</i> as <i>Enterobacter dissolvens</i> comb. nov. and <i>Enterobacter nimipressuralis</i> comb. nov. <i> J.Clin.Microbiol. </i><b> 23 </b>: 1114-1120 ."
        },
        {
          "pubmed": null,
          "reference": "(1988). Validation of the publication of new names and new combinations previously effectively published outside the IJSB. List No. 25. <i> Int.J.Syst.Bacteriol. </i><b> 38 </b>: 220-222 ."
        }
      ],
      "correct_name": null,
      "synonyms": [
        {
          "synonym_type": "heterotypic syn.",
          "synonym": "<i>Enterobacter</i> <i>muelleri</i> "
        }
      ],
      "type_strain": [
        "1497-78",
        "ATCC 35953",
        "DSM 17506",
        "CCUG 25588",
        "CCUG 25714",
        "CIP 103358",
        "JCM 6051",
        "NCTC 12123",
        "strain 1497-78"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterobacter+asburiae"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775932/",
      "pnu_no": 775932,
      "label": "Enterobacter cancerogenus",
      "species": "Enterobacter cancerogenus",
      "species_epithet": "cancerogenus",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "(Urosevic 1966) Dickey and Zumoff 1988",
      "taxon": "comb. nov. (VP)",
      "reference": "Int. J. Syst. Bacteriol. 38:371*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-17580.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Urosevic, B. (1966). Rakovina topolü Püsobena-bakterii <i>Erwinia cancerogena</i> n. sp. <i> Lesnicky Casopsis </i><b> 12 </b>: 493-505 ."
        },
        {
          "pubmed": null,
          "reference": "Dickey, R. S., Zumoff, C. H. (1988). Emended description of <i>Enterobacter cancerogenus</i> comb. nov. (formerly <i>Erwinia cancerogena</i>). <i> Int.J.Syst.Bacteriol. </i><b> 38 </b>: 371-374 ."
        }
      ],
      "correct_name": null,
      "synonyms": [
        {
          "synonym_type": "heterotypic syn.",
          "synonym": "<i>Enterobacter</i> <i>taylorae</i> "
        },
        {
          "synonym_type": "basonym",
          "synonym": "<i>Erwinia</i> <i>cancerogena</i> "
        }
      ],
      "type_strain": [
        "NCPPB 2176",
        "DSM 17580",
        "ATCC 33241",
        "CCUG 25231",
        "CFBP 4167",
        "CIP 103787",
        "ICMP 5706",
        "LMG 2693"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterobacter+cancerogenus"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775933/",
      "pnu_no": 775933,
      "label": "Enterobacter cloacae",
      "species": "Enterobacter cloacae",
      "species_epithet": "cloacae",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "(Jordan 1890) Hormaeche and Edwards 1960",
      "taxon": "comb. nov. (AL)",
      "reference": "Int. J. Syst. Bacteriol. 30:225",
      "comment": "[DSMZ] divided into subspecies",
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-30054.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Hormaeche, E., Edwards, P. R. (1960). A proposed genus <i>Enterobacter</i>. <i> Int.Bull.Bacteriol.Nomencl.Taxon. </i><b> 10 </b>: 71-74 ."
        },
        {
          "pubmed": null,
          "reference": "Jordan, E. O., (1890). A report on certain species of bacteria observed in sewage. In <i> The Report of the Massachusetts Board of Health </i>, pp. 821-844. Edited by W. T. Sedgewick,"
        }
      ],
      "correct_name": null,
      "synonyms": [
        {
          "synonym_type": "homotypic syn.",
          "synonym": "<i>Enterobacter</i> <i>cloacae</i> subsp. <i>cloacae</i> "
        }
      ],
      "type_strain": [
        "ATCC 13047",
        "DSM 30054",
        "CCUG 28448",
        "CCUG 29301",
        "CCUG 6323",
        "CIP 60.85",
        "DSMZ 30054",
        "HAMBI 1295",
        "HAMBI 96",
        "IFO 13535",
        "JCM 1232",
        "LMG 2783",
        "NBRC 13535",
        "NCTC 10005"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterobacter+cloacae"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775934/",
      "pnu_no": 775934,
      "label": "Enterobacter cloacae subsp. cloacae",
      "species": "Enterobacter cloacae subsp. cloacae",
      "species_epithet": "cloacae",
      "subspecies_epithet": "cloacae",
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "(Jordan 1890) Hoffmann et al. 2005",
      "taxon": "comb. nov. (VL), homotypic syn.",
      "reference": "Int. J. Syst. Evol. Microbiol. 55:1395",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-30054.html",
      "literature": [
        {
          "pubmed": "16014455",
          "reference": "(2005). Validation of publication of new names and new combinations previously effectively published outside the IJSEM. List No. 104. <i> Int.J.Syst.Evol.Microbiol. </i><b> 55 </b>: 1395-1397 ."
        },
        {
          "pubmed": "15900966",
          "reference": "Hoffmann, H., Stindl, S., Ludwig, W., Stumpf, A., Mehlen, A., Heesemann, J., Monget, D., Schleifer, K. H., Roggenkamp, A. (2005). Reassignment of <i>Enterobacter dissolvens</i> to <i>Enterobacter cloacae</i> as <i>E. cloacae</i> subspecies <i>dissolvens</i> comb. nov. and emended description of <i> Enterobacter asburiae</i> and <i>Enterobacter kobei.</i>. <i> Syst.Appl.Microbiol. </i><b> 28 </b>: 196-205 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/775933/",
        "Enterobacter cloacae"
      ],
      "synonyms": null,
      "type_strain": [
        "ATCC 13047",
        "CIP 60.85",
        "DSM 30054",
        "JCM 1232",
        "LMG 2783",
        "CCUG 28448",
        "CCUG 29301",
        "CCUG 6323",
        "DSMZ 30054",
        "HAMBI 1295",
        "HAMBI 96",
        "IFO 13535",
        "NBRC 13535",
        "NCTC 10005"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterobacter+cloacae"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775935/",
      "pnu_no": 775935,
      "label": "Enterobacter cloacae subsp. dissolvens",
      "species": "Enterobacter cloacae subsp. dissolvens",
      "species_epithet": "cloacae",
      "subspecies_epithet": "dissolvens",
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "(Rosen 1922) Hoffmann et al. 2005",
      "taxon": "comb. nov. (VL)",
      "reference": "Int. J. Syst. Evol. Microbiol. 55:1395",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-16657.html",
      "literature": [
        {
          "pubmed": "16014455",
          "reference": "(2005). Validation of publication of new names and new combinations previously effectively published outside the IJSEM. List No. 104. <i> Int.J.Syst.Evol.Microbiol. </i><b> 55 </b>: 1395-1397 ."
        },
        {
          "pubmed": "15900966",
          "reference": "Hoffmann, H., Stindl, S., Ludwig, W., Stumpf, A., Mehlen, A., Heesemann, J., Monget, D., Schleifer, K. H., Roggenkamp, A. (2005). Reassignment of <i>Enterobacter dissolvens</i> to <i>Enterobacter cloacae</i> as <i>E. cloacae</i> subspecies <i>dissolvens</i> comb. nov. and emended description of <i> Enterobacter asburiae</i> and <i>Enterobacter kobei.</i>. <i> Syst.Appl.Microbiol. </i><b> 28 </b>: 196-205 ."
        },
        {
          "pubmed": "3711302",
          "reference": "Brenner, D. J., McWhorter, A. C., Kai, A., Steigerwalt, A. G., Farmer, J. J. (1986). <i>Enterobacter asburiae</i> sp. nov., a new species found in clinical specimens, and reassignement of <i>Erwinia dissolvens</i> and <i>Erwinia nimipressuralis</i> to the genus <i>Enterobacter</i> as <i>Enterobacter dissolvens</i> comb. nov. and <i>Enterobacter nimipressuralis</i> comb. nov. <i> J.Clin.Microbiol. </i><b> 23 </b>: 1114-1120 ."
        },
        {
          "pubmed": null,
          "reference": "(1988). Validation of the publication of new names and new combinations previously effectively published outside the IJSB. List No. 25. <i> Int.J.Syst.Bacteriol. </i><b> 38 </b>: 220-222 ."
        }
      ],
      "correct_name": null,
      "synonyms": [
        {
          "synonym_type": "homotypic syn.",
          "synonym": "<i>Enterobacter</i> <i>dissolvens</i> "
        },
        {
          "synonym_type": "basonym",
          "synonym": "<i>Erwinia</i> <i>dissolvens</i> "
        }
      ],
      "type_strain": [
        "ATCC 23373",
        "CIP 105586",
        "JCM 6049",
        "LMG 2683",
        "DSM 16657",
        "CCUG 25230",
        "ICMP 1570",
        "NCPPB 1850"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterobacter+cloacae+subsp.+dissolvens"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775936/",
      "pnu_no": 775936,
      "label": "Enterobacter cowanii",
      "species": "Enterobacter cowanii",
      "species_epithet": "cowanii",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Inoue et al. 2001",
      "taxon": "sp. nov. (VL)",
      "reference": "Int. J. Syst. Evol. Microbiol. 51:1619",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-18146.html",
      "literature": [
        {
          "pubmed": "11080391",
          "reference": "Inoue, K., Sugiyama, K., Kosako, Y., Sakazaki, R., Yamai, S. (2000). <i>Enterobacter cowanii</i> sp. nov., a new species of the family <i>Enterobacteriaceae</i>. <i> Curr.Microbiol. </i><b> 41 </b>: 417-420 ."
        },
        {
          "pubmed": "11594587",
          "reference": "(2001). Validation of publication of new names and new combinations previously effectively published outside the IJSEM. List No. 82. <i> Int.J.Syst.Evol.Microbiol. </i><b> 51 </b>: 1619-1620 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/791223/",
        "Kosakonia cowanii"
      ],
      "synonyms": null,
      "type_strain": [
        "888-76",
        "JCM 10956",
        "CCUG 45998 A",
        "CCUG 45998 B",
        "CIP 107300",
        "DSM 18146"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Kosakonia+cowanii"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775937/",
      "pnu_no": 775937,
      "label": "Enterobacter dissolvens",
      "species": "Enterobacter dissolvens",
      "species_epithet": "dissolvens",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "(Rosen 1922) Brenner et al. 1988",
      "taxon": "comb. nov. (VL), homotypic syn.",
      "reference": "Int. J. Syst. Bacteriol. 38:220",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-16657.html",
      "literature": [
        {
          "pubmed": "3711302",
          "reference": "Brenner, D. J., McWhorter, A. C., Kai, A., Steigerwalt, A. G., Farmer, J. J. (1986). <i>Enterobacter asburiae</i> sp. nov., a new species found in clinical specimens, and reassignement of <i>Erwinia dissolvens</i> and <i>Erwinia nimipressuralis</i> to the genus <i>Enterobacter</i> as <i>Enterobacter dissolvens</i> comb. nov. and <i>Enterobacter nimipressuralis</i> comb. nov. <i> J.Clin.Microbiol. </i><b> 23 </b>: 1114-1120 ."
        },
        {
          "pubmed": null,
          "reference": "(1988). Validation of the publication of new names and new combinations previously effectively published outside the IJSB. List No. 25. <i> Int.J.Syst.Bacteriol. </i><b> 38 </b>: 220-222 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/775935/",
        "Enterobacter cloacae subsp. dissolvens"
      ],
      "synonyms": [
        {
          "synonym_type": "basonym",
          "synonym": "<i>Erwinia</i> <i>dissolvens</i> "
        }
      ],
      "type_strain": [
        "ATCC 23373",
        "DSM 16657",
        "CCUG 25230",
        "CIP 105586",
        "ICMP 1570",
        "JCM 6049",
        "LMG 2683",
        "NCPPB 1850"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterobacter+cloacae+subsp.+dissolvens"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775939/",
      "pnu_no": 775939,
      "label": "Enterobacter gergoviae",
      "species": "Enterobacter gergoviae",
      "species_epithet": "gergoviae",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Brenner et al. 1980",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Bacteriol. 30:1*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-9245.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Brenner, D. J., Richard, C., Steigerwalt, A. G., Asbury, M. A., Mandel, M. (1980). <i>Enterobacter gergoviae</i> sp.nov.: A new species of <i>Enterobacteriaceae </i>found in clinical specimens and the environment. <i> Int.J.Syst.Bacteriol. </i><b> 30 </b>: 1-6 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/791221/",
        "Pluralibacter gergoviae"
      ],
      "synonyms": null,
      "type_strain": [
        "ATCC 33028",
        "CDC 604-77",
        "CIP 76.01",
        "DSM 9245",
        "CCUG 14557",
        "CIP 76. 01",
        "DSMZ 9245",
        "JCM 1234",
        "LMG 5739",
        "NCTC 11434"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Pluralibacter+gergoviae"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775940/",
      "pnu_no": 775940,
      "label": "Enterobacter helveticus",
      "species": "Enterobacter helveticus",
      "species_epithet": "helveticus",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Stephan et al. 2007",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 57:820*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-18396.html",
      "literature": [
        {
          "pubmed": "17392213",
          "reference": "Stephan, R., Van Trappen, S., Cleenwerck, I., Vancanneyt, M., De Vos, P., Lehner, A. (2007). <i>Enterobacter turicensis</i> sp. nov. and <i>Enterobacter helveticus</i> sp. nov., isolated from fruit powder. <i> Int.J.Syst.Evol.Microbiol. </i><b> 57 </b>: 820-826 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/792220/",
        "Franconibacter helveticus"
      ],
      "synonyms": [
        {
          "synonym_type": "homotypic syn.",
          "synonym": "<i>Cronobacter</i> <i>helveticus</i> "
        }
      ],
      "type_strain": [
        "513/05",
        "LMG 23732",
        "DSM 18396",
        "JCM 16470"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Franconibacter+helveticus"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775942/",
      "pnu_no": 775942,
      "label": "Enterobacter hormaechei subsp. hormaechei",
      "species": "Enterobacter hormaechei subsp. hormaechei",
      "species_epithet": "hormaechei",
      "subspecies_epithet": "hormaechei",
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "(O'Hara et al. 1990) Hoffmann et al. 2016",
      "taxon": "comb. nov. (VL), homotypic syn.",
      "reference": "Int. J. Syst. Evol. Microbiol. 66:4299",
      "comment": "[IJSEM] Syllabification and etymology must be adjusted as follows: (hor.maeu02019che.i. N.L. gen. n. hormaechei after Estenio Hormaeche u02026); the name is not a comb. nov. as stated by the authors. // The effective publication states that the type strain was also deposited as CCUG 27126, but no documentation was supplied.",
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-12409.html",
      "literature": null,
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/783768/",
        "Enterobacter hormaechei"
      ],
      "synonyms": null,
      "type_strain": [
        "ATCC 49162",
        "CIP 103441",
        "CCUG 27126",
        "DSM 12409",
        "0992-77",
        "0992-77; ATCC 49162; CIP 103441; CCUG 27126"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterobacter+hormaechei"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775943/",
      "pnu_no": 775943,
      "label": "Enterobacter hormaechei subsp. oharae",
      "species": "Enterobacter hormaechei subsp. oharae",
      "species_epithet": "hormaechei",
      "subspecies_epithet": "oharae",
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Hoffmann et al. 2016",
      "taxon": "subsp. nov. (VL)",
      "reference": "Int. J. Syst. Evol. Microbiol. 66:4299",
      "comment": "[DSMZ] in the effective publication, the DSMZ collection number of the type strain was mistakenly given as DSMZ 16687 instead of DSM 16687 // [IJSEM] Syllabification and etymology must be adjusted as follows: (o.hau02019rae. N.L. gen. n. oharae in honor of Caroline M. Ou02019Hara u02026). // The authors gave DSMZ instead of DSM.",
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-16687.html",
      "literature": null,
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "EN-314",
        "CIP 108490",
        "DSM 16687",
        "EN-314; DSM 16687; CIP 108490"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterobacter+hormaechei+subsp.+oharae"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775944/",
      "pnu_no": 775944,
      "label": "Enterobacter hormaechei subsp. steigerwaltii",
      "species": "Enterobacter hormaechei subsp. steigerwaltii",
      "species_epithet": "hormaechei",
      "subspecies_epithet": "steigerwaltii",
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Hoffmann et al. 2016",
      "taxon": "subsp. nov. (VL)",
      "reference": "Int. J. Syst. Evol. Microbiol. 66:4299",
      "comment": "[DSMZ] in the effective publication, the DSMZ collection number of the type strain was mistakenly given as DSMZ 16691 instead of DSM 16691 // [IJSEM] Syllabification and etymology must be adjusted as follows: (stei.ger.walu02019ti.i. N.L. gen. n. steigerwaltii in honor of Arnold G. Steigerwalt u02026). // The authors gave DSMZ instead of DSM.",
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-16691.html",
      "literature": null,
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "EN-562",
        "CIP 108489",
        "DSM 16691",
        "EN-562; DSM 16691; CIP 108489"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterobacter+hormaechei+subsp.+steigerwaltii"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775945/",
      "pnu_no": 775945,
      "label": "Enterobacter intermedius",
      "species": "Enterobacter intermedius",
      "species_epithet": "intermedius",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "corrig. Izard et al. 1980",
      "taxon": "sp. nov. (VL)",
      "reference": "Int. J. Syst. Bacteriol. 30:601",
      "comment": "[DSMZ] nom. corrig.: IJSB 40:211*",
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-4581.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Izard, D. F., Gavini, F., Leclerc, H. (1980). Polynucleotide sequence relatedness and genome size among <i>Enterobacter intermedium</i> sp. nov. and the species <i>Enterobacter cloacae</i> and <i>Klebsiella pneumoniae</i>. <i> Zbl.Bakt.Hyg., I.Abt.Orig.C </i><b> 1 </b>: 51-60 ."
        },
        {
          "pubmed": null,
          "reference": "(1980). Validation of the publication of new names and new combinations previously effectively published outside the IJSB. List No. 4. <i> Int.J.Syst.Bacteriol. </i><b> 30 </b>: 601 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/777172/",
        "Kluyvera intermedia"
      ],
      "synonyms": [
        {
          "synonym_type": "heterotypic syn.",
          "synonym": "<i>Kluyvera</i> <i>cochleae</i> "
        },
        {
          "synonym_type": "orthographically incorrect name, homotypic syn.",
          "synonym": "<i>Enterobacter</i> <i>intermedium</i> "
        }
      ],
      "type_strain": [
        "ATCC 33110",
        "CIP 79-27",
        "CIP 79.27",
        "CUETM 77-130",
        "DSM 4581",
        "Gavini E 86",
        "CCUG 14183",
        "HAMBI 1299",
        "JCM 1238",
        "LMG 2785",
        "NBRC 102594",
        "NCTC 12125"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Kluyvera+intermedia"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775946/",
      "pnu_no": 775946,
      "label": "Enterobacter kobei",
      "species": "Enterobacter kobei",
      "species_epithet": "kobei",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Kosako et al. 1997 emend. Hoffmann et al. 2005",
      "taxon": "sp. nov. (VL)",
      "reference": "Int. J. Syst. Bacteriol. 47:915",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-13645.html",
      "literature": [
        {
          "pubmed": "16014457",
          "reference": "(2005). Notification of changes in taxonomic opinion previously published outside the IJSEM. No. 2. <i> Int.J.Syst.Evol.Microbiol. </i><b> 55 </b>: 1403-1404 ."
        },
        {
          "pubmed": "15900966",
          "reference": "Hoffmann, H., Stindl, S., Ludwig, W., Stumpf, A., Mehlen, A., Heesemann, J., Monget, D., Schleifer, K. H., Roggenkamp, A. (2005). Reassignment of <i>Enterobacter dissolvens</i> to <i>Enterobacter cloacae</i> as <i>E. cloacae</i> subspecies <i>dissolvens</i> comb. nov. and emended description of <i> Enterobacter asburiae</i> and <i>Enterobacter kobei.</i>. <i> Syst.Appl.Microbiol. </i><b> 28 </b>: 196-205 ."
        },
        {
          "pubmed": null,
          "reference": "Kosako, Y., Tamura, K., Sakazaki, R., Miki, K. (1996). <i>Enterobacter kobei</i> sp. nov., a new species of the family <i>Enterobacteriaceae</i> resembling <i>Enterobacter cloacae</i>. <i> Curr Microbiol. </i><b> 33 </b> ( 4 ): 261-265 ."
        },
        {
          "pubmed": "8824173",
          "reference": "Kosako, Y., Tamura, K., Sakazaki, R., Miki, K. (1996). <i>Enterobacter kobei</i> sp. nov., a new species of the family <i>Enterobacteriaceae</i> resembling <i>Enterobacter cloacae</i>. <i> Curr.Microbiol. </i><b> 33 </b>: 261-265 ."
        },
        {
          "pubmed": null,
          "reference": "(1997). Validation of the publication of new names and new combinations previously effectively published outside the IJSB. List No. 62. <i> Int.J.Syst.Bacteriol. </i><b> 47 </b>: 915-916 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "JCM 8580",
        "NIH 1485-79",
        "DSM 13645",
        "DSM 27110",
        "CCUG 49023",
        "CIP 105566",
        "strain ATCC BAA-260"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterobacter+kobei"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775948/",
      "pnu_no": 775948,
      "label": "Enterobacter ludwigii",
      "species": "Enterobacter ludwigii",
      "species_epithet": "ludwigii",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Hoffmann et al. 2005",
      "taxon": "sp. nov. (VL)",
      "reference": "Int. J. Syst. Evol. Microbiol. 55:2235",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-16688.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "(2005). Validation of publication of new names and new combinations previously effectively published outside the IJSEM - List no. 106. <i> Int.J.Syst.Evol.Microbiol. </i><b> 55 </b>: 2235-2238 ."
        },
        {
          "pubmed": "15900967",
          "reference": "Hoffmann, H., Stindl, S., Stumpf, A., Mehlen, A., Monget, D., Heesemann, J., Schleifer, K. H., Roggenkamp, A. (2005). Description of <i>Enterobacter ludwigii</i> sp. nov., a novel <i>Enterobacter</i> species of clinical relevance. <i> Syst.Appl.Microbiol. </i><b> 28 </b>: 206-212 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "CIP 108491",
        "DSM 16688",
        "EN-119",
        "CCUG 51323",
        "CCUG 51354"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterobacter+ludwigii"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775950/",
      "pnu_no": 775950,
      "label": "Enterobacter pyrinus",
      "species": "Enterobacter pyrinus",
      "species_epithet": "pyrinus",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Chung et al. 1993",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Bacteriol. 43:157*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-12410.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Chung, Y. R., Brenner, D. J., Steigerwalt, A. G., Kim, B. S., Kim, H. T., Cho, K. Y. (1993). <i>Enterobacter pyrinus</i> sp. nov., an organism associated with brown leaf spot disease of pear trees. <i> Int.J.Syst.Bacteriol. </i><b> 43 </b>: 157-161 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/791222/",
        "Pluralibacter pyrinus"
      ],
      "synonyms": null,
      "type_strain": [
        "DSM 12410",
        "ATCC 49851",
        "CCUG 48320",
        "CDC G6570",
        "CFBP 4168",
        "CIP 104019",
        "ICMP 12530",
        "KCTC 2520",
        "LMG 22970"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Pluralibacter+pyrinus"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775951/",
      "pnu_no": 775951,
      "label": "Enterobacter radicincitans",
      "species": "Enterobacter radicincitans",
      "species_epithet": "radicincitans",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Kämpfer et al. 2005",
      "taxon": "sp. nov. (VL)",
      "reference": "Int. J. Syst. Evol. Microbiol. 55:1395",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-16656.html",
      "literature": [
        {
          "pubmed": "16014455",
          "reference": "(2005). Validation of publication of new names and new combinations previously effectively published outside the IJSEM. List No. 104. <i> Int.J.Syst.Evol.Microbiol. </i><b> 55 </b>: 1395-1397 ."
        },
        {
          "pubmed": "15900968",
          "reference": "Kämpfer, P., Ruppel, S., Remus, R. (2005). <i>Enterobacter radicincitans</i> sp. nov., a plant growth promoting species of the family <i>Enterobacteriaceae.</i>. <i> Syst.Appl.Microbiol. </i><b> 28 </b>: 213-221 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/791224/",
        "Kosakonia radicincitans"
      ],
      "synonyms": null,
      "type_strain": [
        "CIP 108468",
        "D5/23",
        "DSM 16656",
        "CCUG 50898"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Kosakonia+radicincitans"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775952/",
      "pnu_no": 775952,
      "label": "Enterobacter sakazakii",
      "species": "Enterobacter sakazakii",
      "species_epithet": "sakazakii",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Farmer et al. 1980",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Bacteriol. 30:569*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-4485.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Farmer, J. J., Asbury, M. A., Hickman, F. W., Brenner, D. J. (1980). <i>Enterobacter sakazakii</i>: a new secies of \"<i>Enterobacteriaceae</i>\" isolated from clinical specimens. <i> Int.J.Syst.Bacteriol. </i><b> 30 </b>: 569-584 ."
        }
      ],
      "correct_name": null,
      "synonyms": [
        {
          "synonym_type": "homotypic syn.",
          "synonym": "<i>Cronobacter</i> <i>sakazakii</i> "
        },
        {
          "synonym_type": "homotypic syn.",
          "synonym": "\"<i>Cronobacter sakazakii</i>\" subsp. <i>sakazakii</i> "
        }
      ],
      "type_strain": [
        "ATCC 29544",
        "CDC 4562-70",
        "DSM 4485",
        "CCUG 14558",
        "CIP 103183",
        "DSMZ 4485",
        "JCM 1233",
        "LMG 5740",
        "NBRC 102416",
        "NCTC 11467"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterobacter+sakazakii"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775954/",
      "pnu_no": 775954,
      "label": "Enterobacter turicensis",
      "species": "Enterobacter turicensis",
      "species_epithet": "turicensis",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Stephan et al. 2007",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 57:820*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-18397.html",
      "literature": [
        {
          "pubmed": "17392213",
          "reference": "Stephan, R., Van Trappen, S., Cleenwerck, I., Vancanneyt, M., De Vos, P., Lehner, A. (2007). <i>Enterobacter turicensis</i> sp. nov. and <i>Enterobacter helveticus</i> sp. nov., isolated from fruit powder. <i> Int.J.Syst.Evol.Microbiol. </i><b> 57 </b>: 820-826 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/792219/",
        "Siccibacter turicensis"
      ],
      "synonyms": [
        {
          "synonym_type": "homotypic syn.",
          "synonym": "<i>Cronobacter</i> <i>zurichensis</i> "
        }
      ],
      "type_strain": [
        "508/05",
        "LMG 23730",
        "DSM 18397",
        "JCM 16472",
        "508/05; DSM 18397; JCM 16472; LMG 23730"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Siccibacter+turicensis"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775955/",
      "pnu_no": 775955,
      "label": "Enterococcus aquimarinus",
      "species": "Enterococcus aquimarinus",
      "species_epithet": "aquimarinus",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "&#x0160;vec et al. 2005",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 55:2183*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-17690.html",
      "literature": [
        {
          "pubmed": "16166729",
          "reference": "Svec, P., Vancanneyt, M., Devriese, L. A., Naser, S. M., Snauwaert, C., Lefebvre, K., Hoste, B., Swings, J. (2005). <i>Enterococcus aquimarinus</i> sp. nov., isolated from sea water. <i> Int.J.Syst.Evol.Microbiol. </i><b> 55 </b>: 2183-2187 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "CCM 7283",
        "LMG 16607",
        "DSM 17690",
        "API 8407116",
        "CCUG 51308"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+aquimarinus"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775956/",
      "pnu_no": 775956,
      "label": "Enterococcus asini",
      "species": "Enterococcus asini",
      "species_epithet": "asini",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "de Vaux et al. 1998",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Bacteriol. 48:383*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-11492.html",
      "literature": [
        {
          "pubmed": "9731276",
          "reference": "de Vaux, A., Laguerre, G., Diviès, C., Prévost, H. (1998). <i>Enterococcus asini</i> sp. nov. isolated from the caecum of donkeys (<i>Equus asinus</i>). <i> Int.J.Syst.Bacteriol. </i><b> 48 </b>: 383-387 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "AS2",
        "DSM 11492",
        "ATCC 700915",
        "CCUG 44928",
        "LMG 18727",
        "NBRC 100681",
        "strain AS2"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+asini"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775957/",
      "pnu_no": 775957,
      "label": "Enterococcus avium",
      "species": "Enterococcus avium",
      "species_epithet": "avium",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "(ex Nowlan and Deibel 1967) Collins et al. 1984",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Bacteriol. 34:220*",
      "comment": "[DSMZ] basonym \"<I>Streptococcus avium</I>\"",
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-20679.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Collins, M. D., Jones, D., Farrow, J. A. E., Kilpper-Bälz, R., Schleifer, K. H. (1984). <i>Enterococcus avium</i> nom. rev., comb. nov.; <i>E. casseliflavus</i> nom. rev., comb. nov.; <i>E. durans</i> nom. rev., comb. nov.;<i> E. gallinarum</i> comb. nov.; and <i>E. malodoratus </i>sp. nov. <i> Int.J.Syst.Bacteriol. </i><b> 34 </b>: 220-223 ."
        }
      ],
      "correct_name": null,
      "synonyms": [
        {
          "synonym": "\"<i>Streptococcus avium</i>\""
        }
      ],
      "type_strain": [
        "ATCC 14025",
        "DSM 20679",
        "Guthof  6844",
        "IMET 3257",
        "NCDO 2369",
        "NCTC 9938",
        "CCUG 7983",
        "CIP 103019",
        "CIP 103 019",
        "DSMZ 20679",
        "Guthof E6844",
        "JCM 8722",
        "LMG 10744",
        "NBRC 100477",
        "NCIMB 702369",
        "VKM B-1673"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+avium"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775958/",
      "pnu_no": 775958,
      "label": "Enterococcus canis",
      "species": "Enterococcus canis",
      "species_epithet": "canis",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "De Graef et al. 2003",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 53:1069*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-17029.html",
      "literature": [
        {
          "pubmed": "12892128",
          "reference": "De Graef, E. M., Devriese, L. A., Vancanneyt, M., Baele, M., Collins, M. D., Lefebvre, K., Swings, J., Haesebrouck, F. (2003). Description of<i> Enterococcus canis</i> sp. nov. from dogs and reclassification of<i> Enterococcus porcinus</i> Teixeira et al. 2001 as a junior synonym of<i> Enterococcus villorum</i> Vancanneyt et al. 2001. <i> Int.J.Syst.Evol.Microbiol. </i><b> 53 </b>: 1069-1074 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "CCUG 46666",
        "LMG 12316",
        "DSM 17029",
        "NBRC 100695"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+canis"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775959/",
      "pnu_no": 775959,
      "label": "Enterococcus casseliflavus",
      "species": "Enterococcus casseliflavus",
      "species_epithet": "casseliflavus",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "(ex Vaughn et al. 1979) Collins et al. 1984",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Bacteriol. 34:220*",
      "comment": "[DSMZ] basonym \"<I>Streptococcus faecium</I> subsp. <I>casseliflavus</I>\"",
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-20680.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Collins, M. D., Jones, D., Farrow, J. A. E., Kilpper-Bälz, R., Schleifer, K. H. (1984). <i>Enterococcus avium</i> nom. rev., comb. nov.; <i>E. casseliflavus</i> nom. rev., comb. nov.; <i>E. durans</i> nom. rev., comb. nov.;<i> E. gallinarum</i> comb. nov.; and <i>E. malodoratus </i>sp. nov. <i> Int.J.Syst.Bacteriol. </i><b> 34 </b>: 220-223 ."
        }
      ],
      "correct_name": null,
      "synonyms": [
        {
          "synonym_type": "heterotypic syn.",
          "synonym": "<i>Enterococcus</i> <i>flavescens</i> "
        },
        {
          "synonym_type": "basonym",
          "synonym": "\"<i>Streptococcus casseliflavus</i>\" "
        },
        {
          "synonym": "\"<i>Streptococcus faecium</i>\" subsp. <i>casseliflavus</i>"
        }
      ],
      "type_strain": [
        "ATCC 25788",
        "DSM 20680",
        "LMG 10745",
        "MUTK 20",
        "NCDO 2372",
        "CCUG 18657",
        "CIP 103018",
        "DSMZ 20680",
        "JCM 8723",
        "NBRC 100478",
        "NCIMB 11449",
        "NCTC 12361",
        "NRRL B-3502"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+casseliflavus"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775960/",
      "pnu_no": 775960,
      "label": "Enterococcus cecorum",
      "species": "Enterococcus cecorum",
      "species_epithet": "cecorum",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "(Devriese et al. 1983) Williams et al. 1989",
      "taxon": "comb. nov. (VL)",
      "reference": "Int. J. Syst. Bacteriol. 39:495",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-20682.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Williams, A. M., Farrow, J. A. E., Collins, M. D. (1989). Reverse transcriptase sequencing of 16S ribosomal RNA from <i>Streptococcus</i> <i>cecorum</i>. <i> Lett.Appl.Microbiol. </i><b> 8 </b>: 185-189 ."
        },
        {
          "pubmed": null,
          "reference": "(1989). Validation of the publication of new names and new combinations previously effectively published outside the IJSB. List No. 31. <i> Int.J.Syst.Bacteriol. </i><b> 39 </b>: 495-497 ."
        }
      ],
      "correct_name": null,
      "synonyms": [
        {
          "synonym_type": "basonym",
          "synonym": "<i>Streptococcus</i> <i>cecorum</i> "
        }
      ],
      "type_strain": [
        "A60",
        "ATCC 43198",
        "DSM 20682",
        "NCDO 2674",
        "CCUG 27299",
        "CIP 103676",
        "DSMZ 20682",
        "JCM 8724",
        "LMG 12902",
        "NBRC 100674",
        "NCIMB 702674",
        "NCTC 12421"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+cecorum"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775961/",
      "pnu_no": 775961,
      "label": "Enterococcus columbae",
      "species": "Enterococcus columbae",
      "species_epithet": "columbae",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Devriese et al. 1993",
      "taxon": "sp. nov. (VL)",
      "reference": "Int. J. Syst. Bacteriol. 43:188",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-7374.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Devriese, L. A., Ceyssens, K., Rodrigues, U. M., Collins, M. D. (1990). <i>Enterococcus columbae</i>, a species from pigeon intestines. <i> FEMS Microbiol.Lett. </i><b> 71 </b>: 247-252 ."
        },
        {
          "pubmed": null,
          "reference": "(1993). Validation of the publication of new names and new combinations previously effectively published outside the IJSB. List No. 44. <i> Int.J.Syst.Bacteriol. </i><b> 43 </b>: 188-189 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "DSM 7374",
        "NCIMB 13013",
        "STR 345",
        "ATCC 51263",
        "CCUG 27894",
        "CIP 103675",
        "DSMZ 7374",
        "LMG 11740",
        "NBRC 100677"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+columbae"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775962/",
      "pnu_no": 775962,
      "label": "Enterococcus dispar",
      "species": "Enterococcus dispar",
      "species_epithet": "dispar",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Collins et al. 1991",
      "taxon": "sp. nov. (VL)",
      "reference": "Int. J. Syst. Bacteriol. 41:456",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-6630.html",
      "literature": [
        {
          "pubmed": "1370024",
          "reference": "Collins, M. D., Rodrigues, U. M., Pigott, N. E., Facklam, R. R. (1991). <i>Enterococcus dispar</i> sp. nov. a new <i>Enterococcus</i> species from human sources. <i> Lett.Appl.Microbiol. </i><b> 12 </b>: 95-98 ."
        },
        {
          "pubmed": null,
          "reference": "(1991). Validation of the publication of new names and new combinations previously effectively published outside the IJSB. List No. 38. <i> Int.J.Syst.Bacteriol. </i><b> 41 </b>: 456-457 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "DSM 6630",
        "E18-1",
        "NCFB 2821",
        "NCIMB 13000",
        "ATCC 51266",
        "CCUG 33309",
        "CIP 103646",
        "DSMZ 6630",
        "HAMBI 2231",
        "LMG 13521",
        "NBRC 100678",
        "strain E18-1"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+dispar"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775963/",
      "pnu_no": 775963,
      "label": "Enterococcus durans",
      "species": "Enterococcus durans",
      "species_epithet": "durans",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "(ex Sherman and Wing 1937) Collins et al. 1984",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Bacteriol. 34:220*",
      "comment": "[DSMZ] basonym \"<I>Streptococcus durans</I>\"",
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-20633.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Collins, M. D., Jones, D., Farrow, J. A. E., Kilpper-Bälz, R., Schleifer, K. H. (1984). <i>Enterococcus avium</i> nom. rev., comb. nov.; <i>E. casseliflavus</i> nom. rev., comb. nov.; <i>E. durans</i> nom. rev., comb. nov.;<i> E. gallinarum</i> comb. nov.; and <i>E. malodoratus </i>sp. nov. <i> Int.J.Syst.Bacteriol. </i><b> 34 </b>: 220-223 ."
        }
      ],
      "correct_name": null,
      "synonyms": [
        {
          "synonym_type": "homotypic syn.",
          "synonym": "<i>Streptococcus</i> <i>durans</i> "
        }
      ],
      "type_strain": [
        "98D",
        "ATCC 19432",
        "CCM 5612",
        "DSM 20633",
        "NCDO 596",
        "NCTC 8307",
        "DSMZ 20633"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+durans"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775964/",
      "pnu_no": 775964,
      "label": "Enterococcus faecalis",
      "species": "Enterococcus faecalis",
      "species_epithet": "faecalis",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "(Andrewes and Horder 1906) Schleifer and Kilpper-Bälz 1984",
      "taxon": "comb. nov. (VP)",
      "reference": "Int. J. Syst. Bacteriol. 34:31*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-20478.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Andrewes, F. W., Horder, T. J. (1906). A study of the streptococci pathogenic for man. <i> Lancet </i><b> 2 </b>: 708-713 ."
        },
        {
          "pubmed": null,
          "reference": "Schleifer, K. H., Kilpper-Bälz, R. (1984). Transfer of <i>Streptococcus faecalis</i> and <i>Streptococcus faecium</i> to the genus <i>Enterococcus</i> nom. rev. as <i>Enterococcus faecalis</i> comb. nov. and <i>Enterococcus faecium</i> comb. nov. <i> Int.J.Syst.Bacteriol. </i><b> 34 </b>: 31-34 ."
        }
      ],
      "correct_name": null,
      "synonyms": [
        {
          "synonym_type": "basonym",
          "synonym": "<i>Streptococcus</i> <i>faecalis</i> "
        }
      ],
      "type_strain": [
        "ATCC 19433",
        "DSM 20478",
        "NCDO 581",
        "NCIB 775",
        "NCTC 775",
        "ATCC 19433-U",
        "CCUG 19916",
        "CIP 103015",
        "DSM 100701",
        "DSM 100702",
        "DSMZ 20478",
        "HAMBI 1711",
        "JCM 5803",
        "JCM 8726",
        "LMG 7937",
        "NBRC 100480",
        "NBRC 100481",
        "NCAIM B.01312",
        "NCIMB 775"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+faecalis"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775965/",
      "pnu_no": 775965,
      "label": "Enterococcus faecium",
      "species": "Enterococcus faecium",
      "species_epithet": "faecium",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "(Orla-Jensen 1919) Schleifer and Kilpper-Bälz 1984",
      "taxon": "comb. nov. (VP)",
      "reference": "Int. J. Syst. Bacteriol. 34:31*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-20477.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Schleifer, K. H., Kilpper-Bälz, R. (1984). Transfer of <i>Streptococcus faecalis</i> and <i>Streptococcus faecium</i> to the genus <i>Enterococcus</i> nom. rev. as <i>Enterococcus faecalis</i> comb. nov. and <i>Enterococcus faecium</i> comb. nov. <i> Int.J.Syst.Bacteriol. </i><b> 34 </b>: 31-34 ."
        },
        {
          "pubmed": null,
          "reference": "Orla-Jensen, S., (1919). The lactic acid bacteria. Host & Son."
        }
      ],
      "correct_name": null,
      "synonyms": [
        {
          "synonym_type": "basonym",
          "synonym": "<i>Streptococcus</i> <i>faecium</i> "
        }
      ],
      "type_strain": [
        "ATCC 19434",
        "DSM 20477",
        "NCDO 942",
        "NCTC 7171",
        "CCUG 542",
        "CFBP 4248",
        "CIP 103014",
        "DSMZ 20477",
        "HAMBI 1710",
        "JCM 5804",
        "JCM 8727",
        "LMG 11423",
        "NBRC 100485",
        "NBRC 100486",
        "NCIMB 11508"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+faecium"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775966/",
      "pnu_no": 775966,
      "label": "Enterococcus flavescens",
      "species": "Enterococcus flavescens",
      "species_epithet": "flavescens",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Pompei et al. 1992",
      "taxon": "sp. nov. (VP), heterotypic syn.",
      "reference": "Int. J. Syst. Bacteriol. 42:365*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-7370.html",
      "literature": [
        {
          "pubmed": "1503970",
          "reference": "Pompei, R., Berlutti, F., Thaller, M. C., Inginianni, A., Cortis, G., Dainelli, B. (1992). <i>Enterococcus flavescens</i> sp. nov., a new species of enterococci of clinical origin. <i> Int.J.Syst.Bacteriol. </i><b> 42 </b>: 365-369 ."
        },
        {
          "pubmed": "16449449",
          "reference": "Naser, S. M., Vancanneyt, M., Hoste, B., Snauwaert, C., Vandemeulebroecke, K., Swings, J. (2006). Reclassification of <i>Enterococcus flavescens</i> Pompei et al. 1992 as a later synonym of <i>Enterococcus casseliflavus</i> (ex Vaughan et al. 1979) Collins et al. 1984 and <i>Enterococcus saccharominimus</i> Vancanneyt et al. 2004 as a later synonym of <i>Enterococcus italicus</i> Fortina et al. 2004. <i> Int.J.Syst.Evol.Microbiol. </i><b> 56 </b>: 413-416 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/775959/",
        "Enterococcus casseliflavus"
      ],
      "synonyms": [
        {
          "synonym_type": "basonym",
          "synonym": "\"<i>Streptococcus casseliflavus</i>\" "
        },
        {
          "synonym": "\"<i>Streptococcus faecium</i>\" subsp. <i>casseliflavus</i>"
        }
      ],
      "type_strain": [
        "CA 2",
        "CCM 4239",
        "DSM 7370",
        "ATCC 49996",
        "CCUG 30567",
        "CECT 4481",
        "CIP 103525",
        "HAMBI 2233",
        "LMG 13518",
        "NBRC 100679"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+casseliflavus"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775967/",
      "pnu_no": 775967,
      "label": "Enterococcus gallinarum",
      "species": "Enterococcus gallinarum",
      "species_epithet": "gallinarum",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "(Bridge and Sneath 1982) Collins et al. 1984",
      "taxon": "comb. nov. (VP)",
      "reference": "Int. J. Syst. Bacteriol. 34:220*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-20628.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Collins, M. D., Jones, D., Farrow, J. A. E., Kilpper-Bälz, R., Schleifer, K. H. (1984). <i>Enterococcus avium</i> nom. rev., comb. nov.; <i>E. casseliflavus</i> nom. rev., comb. nov.; <i>E. durans</i> nom. rev., comb. nov.;<i> E. gallinarum</i> comb. nov.; and <i>E. malodoratus </i>sp. nov. <i> Int.J.Syst.Bacteriol. </i><b> 34 </b>: 220-223 ."
        },
        {
          "pubmed": null,
          "reference": "Bridge, P. D., Sneath, P. H. A. (1982). <i>Streptococcus gallinarum </i>sp. nov. and <i>Streptococcus oralis </i>sp. nov. <i> Int.J.Syst.Bacteriol. </i><b> 32 </b>: 410-415 ."
        }
      ],
      "correct_name": null,
      "synonyms": [
        {
          "synonym_type": "basonym",
          "synonym": "<i>Streptococcus</i> <i>gallinarum</i> "
        }
      ],
      "type_strain": [
        "ATCC 35038",
        "DSM 20628",
        "F87/276",
        "NCDO 2313",
        "NCTC 11428",
        "PB21",
        "DSM 24841",
        "ATCC 49573",
        "CCUG 18658",
        "CIP 103013",
        "JCM 8728",
        "LMG 13129",
        "NBRC 100675",
        "NCIMB 702313",
        "NCTC 12359",
        "strain PB 21"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+gallinarum"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775968/",
      "pnu_no": 775968,
      "label": "Enterococcus gilvus",
      "species": "Enterococcus gilvus",
      "species_epithet": "gilvus",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Tyrrell et al. 2002",
      "taxon": "sp. nov. (VL)",
      "reference": "Int. J. Syst. Evol. Microbiol. 52:1075",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-15689.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "(2002). Validation of publication of new names and new combinations previously effectively published outside the IJSEM. List No. 86. <i> Int.J.Syst.Evol.Microbiol. </i><b> 52 </b>: 1075-1076 ."
        },
        {
          "pubmed": "11923322",
          "reference": "Tyrrell, G. J., Turnbull, L., Teixeira, L. M., Lefebvre, J., Carvalho, M. G. S., Facklam, R. R., Lovgren, M. (2002). <i>Enterococcus gilvus</i> sp. nov. and <i>Enterococcus pallens</i> sp. nov. isolated from human clinical specimens. <i> J.Clin.Microbiol. </i><b> 40 </b>: 1140-1145 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "ATCC BAA-350",
        "CCUG 45553",
        "PQ1",
        "DSM 15689",
        "NBRC 100696"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+gilvus"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775969/",
      "pnu_no": 775969,
      "label": "Enterococcus haemoperoxidus",
      "species": "Enterococcus haemoperoxidus",
      "species_epithet": "haemoperoxidus",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "&#x0160;vec et al. 2001",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 51:1567*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-15920.html",
      "literature": [
        {
          "pubmed": "11491359",
          "reference": "Svec, P., Devriese, L. A., Sedlácek, I., Baele, M., Vancanneyt, M., Haesebrouck, F., Swings, J., Doskar, J. (2001). <i>Enterococcus haemoperoxidus</i> sp. nov. and <i>Enterococcus moraviensis</i> sp. nov., isolated from water. <i> Int.J.Syst.Evol.Microbiol. </i><b> 51 </b>: 1567-1574 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "440",
        "CCM 4851",
        "LMG 19487",
        "DSM 15920",
        "ATCC BAA-382",
        "CCUG 45916",
        "CIP 107129",
        "NBRC 100709",
        "strain 440"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+haemoperoxidus"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775970/",
      "pnu_no": 775970,
      "label": "Enterococcus hermanniensis",
      "species": "Enterococcus hermanniensis",
      "species_epithet": "hermanniensis",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Koort et al. 2004",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 54:1823*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-17122.html",
      "literature": [
        {
          "pubmed": "15388750",
          "reference": "Koort, J., Coenye, T., Vandamme, P., Sukura, A., Björkroth, J. (2004). <i>Enterococcus hermanniensis</i> sp. nov., from modified-atmosphere-packaged broiler meat and canine tonsils. <i> Int.J.Syst.Evol.Microbiol. </i><b> 54 </b>: 1823-1827 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "CCUG 48100",
        "LMG 12317",
        "DSM 17122"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+hermanniensis"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775971/",
      "pnu_no": 775971,
      "label": "Enterococcus hirae",
      "species": "Enterococcus hirae",
      "species_epithet": "hirae",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Farrow and Collins 1985",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Bacteriol. 35:73*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-20160.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Farrow, J. A. E., Collins, M. D. (1985). <i>Enterococcus hirae</i>, a new species that includes amino acid assay strain NCDO 1258 and strains causing growth depression in young chickens. <i> Int.J.Syst.Bacteriol. </i><b> 35 </b>: 73-75 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "ATCC 8043",
        "CCM 2423",
        "CCM 2424",
        "DSM 20160",
        "IMET 11742",
        "NCDO 1258",
        "NCFP 1258",
        "NCIB 6459",
        "Snell R",
        "ATCC 9790",
        "CCUG 1332",
        "CCUG 18659",
        "CCUG 19917",
        "CFBP 4250",
        "CIP 53.48",
        "E.E. Snell strain R",
        "HAMBI 1709",
        "HAMBI 644",
        "IFO 3181",
        "JCM 8729",
        "LMG 6399",
        "NBRC 3181",
        "NCCB 46070",
        "NCCB 58005",
        "NCIMB 6459",
        "NCTC 12367"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+hirae"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775973/",
      "pnu_no": 775973,
      "label": "Enterococcus italicus",
      "species": "Enterococcus italicus",
      "species_epithet": "italicus",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Fortina et al. 2004",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 54:1717*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-15952.html",
      "literature": [
        {
          "pubmed": "15388734",
          "reference": "Fortina, M. G., Ricci, G., Mora, D., Manachini, P. L. (2004). Molecular analysis of artisanal Italian cheeses reveals <i>Enterococcus italicus</i> sp. nov. <i> Int.J.Syst.Evol.Microbiol. </i><b> 54 </b>: 1717-1721 ."
        }
      ],
      "correct_name": null,
      "synonyms": [
        {
          "synonym_type": "heterotypic syn.",
          "synonym": "<i>Enterococcus</i> <i>saccharominimus</i> "
        }
      ],
      "type_strain": [
        "DSM 15952",
        "LMG 22039",
        "CCUG 50447",
        "TP1.5"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+italicus"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775974/",
      "pnu_no": 775974,
      "label": "Enterococcus malodoratus",
      "species": "Enterococcus malodoratus",
      "species_epithet": "malodoratus",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "(ex Pette 1955) Collins et al. 1984",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Bacteriol. 34:220*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-20681.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Collins, M. D., Jones, D., Farrow, J. A. E., Kilpper-Bälz, R., Schleifer, K. H. (1984). <i>Enterococcus avium</i> nom. rev., comb. nov.; <i>E. casseliflavus</i> nom. rev., comb. nov.; <i>E. durans</i> nom. rev., comb. nov.;<i> E. gallinarum</i> comb. nov.; and <i>E. malodoratus </i>sp. nov. <i> Int.J.Syst.Bacteriol. </i><b> 34 </b>: 220-223 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "DSM 20681",
        "NCDO 846",
        "ATCC 43197",
        "CCUG 30572",
        "CIP 103012",
        "DSMZ 20681",
        "HAMBI 1569",
        "JCM 8730",
        "LMG 10747",
        "NBRC 100489",
        "NCIMB 700846",
        "NCTC 12365"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+malodoratus"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775975/",
      "pnu_no": 775975,
      "label": "Enterococcus moraviensis",
      "species": "Enterococcus moraviensis",
      "species_epithet": "moraviensis",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "&#x0160;vec et al. 2001",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 51:1567*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-15919.html",
      "literature": [
        {
          "pubmed": "11491359",
          "reference": "Svec, P., Devriese, L. A., Sedlácek, I., Baele, M., Vancanneyt, M., Haesebrouck, F., Swings, J., Doskar, J. (2001). <i>Enterococcus haemoperoxidus</i> sp. nov. and <i>Enterococcus moraviensis</i> sp. nov., isolated from water. <i> Int.J.Syst.Evol.Microbiol. </i><b> 51 </b>: 1567-1574 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "330",
        "CCM 4856",
        "LMG 19486",
        "DSM 15919",
        "ATCC BAA-383",
        "CCUG 45913",
        "CIP 107130",
        "NBRC 100710",
        "strain 330"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+moraviensis"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775976/",
      "pnu_no": 775976,
      "label": "Enterococcus mundtii",
      "species": "Enterococcus mundtii",
      "species_epithet": "mundtii",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Collins et al. 1986",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Bacteriol. 36:8*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-4838.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Collins, M. D., Farrow, J. A. E., Jones, D. (1988). <i>Enterococcus mundtii</i> sp. nov. <i> Int.J.Syst.Bacteriol. </i><b> 36 </b>: 8-12 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "DSM 4838",
        "NCDO 2375",
        "ATCC 43186",
        "CCUG 18656",
        "CFBP 4251",
        "CIP 103010",
        "DSMZ 4838",
        "HAMBI 1570",
        "JCM 8731",
        "LMG 10748",
        "MUTK 559",
        "NBRC 100490",
        "NCIMB 702375",
        "NCTC 12363"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+mundtii"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775977/",
      "pnu_no": 775977,
      "label": "Enterococcus pallens",
      "species": "Enterococcus pallens",
      "species_epithet": "pallens",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Tyrrell et al. 2002",
      "taxon": "sp. nov. (VL)",
      "reference": "Int. J. Syst. Evol. Microbiol. 52:1075",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-15690.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "(2002). Validation of publication of new names and new combinations previously effectively published outside the IJSEM. List No. 86. <i> Int.J.Syst.Evol.Microbiol. </i><b> 52 </b>: 1075-1076 ."
        },
        {
          "pubmed": "11923322",
          "reference": "Tyrrell, G. J., Turnbull, L., Teixeira, L. M., Lefebvre, J., Carvalho, M. G. S., Facklam, R. R., Lovgren, M. (2002). <i>Enterococcus gilvus</i> sp. nov. and <i>Enterococcus pallens</i> sp. nov. isolated from human clinical specimens. <i> J.Clin.Microbiol. </i><b> 40 </b>: 1140-1145 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "ATCC BAA-351",
        "CCUG 45554",
        "PQ2",
        "DSM 15690",
        "NBRC 100697"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+pallens"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775978/",
      "pnu_no": 775978,
      "label": "Enterococcus phoeniculicola",
      "species": "Enterococcus phoeniculicola",
      "species_epithet": "phoeniculicola",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Law-Brown and Meyers 2003",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 53:683*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-14726.html",
      "literature": [
        {
          "pubmed": "12807187",
          "reference": "Law-Brown, J., Meyers, P. R. (2003). <i>Enterococcus phoeniculicola</i> sp. nov., a novel member of the enterococci isolated from the uropygial gland of the <i>Red-billed Woodhoopoe</i>, <i>Phoeniculus purpureus</i>. <i> Int.J.Syst.Evol.Microbiol. </i><b> 53 </b>: 683-685 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "ATCC BAA-412",
        "CCUG 48923",
        "DSM 14726",
        "JLB-1",
        "KCTC 3818",
        "NBRC 100711",
        "strain JLB-1"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+phoeniculicola"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775979/",
      "pnu_no": 775979,
      "label": "Enterococcus porcinus",
      "species": "Enterococcus porcinus",
      "species_epithet": "porcinus",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Teixeira et al. 2001",
      "taxon": "sp. nov. (VP), heterotypic syn.",
      "reference": "Int. J. Syst. Evol. Microbiol. 51:1737*",
      "comment": "[DSMZ] synonymy: IJSEM 53:1069*; junior heterotypic synonym of <I>Enterococcus villorum</I>",
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": null,
      "literature": [
        {
          "pubmed": "12892128",
          "reference": "De Graef, E. M., Devriese, L. A., Vancanneyt, M., Baele, M., Collins, M. D., Lefebvre, K., Swings, J., Haesebrouck, F. (2003). Description of<i> Enterococcus canis</i> sp. nov. from dogs and reclassification of<i> Enterococcus porcinus</i> Teixeira et al. 2001 as a junior synonym of<i> Enterococcus villorum</i> Vancanneyt et al. 2001. <i> Int.J.Syst.Evol.Microbiol. </i><b> 53 </b>: 1069-1074 ."
        },
        {
          "pubmed": "11594604",
          "reference": "Teixeira, L. M., Carvalho, M. G. S., Espinola, M. M. B., Steigerwalt, A. G., Douglas, M. P., Brenner, D. J., Facklam, R. R. (2001). <i>Enterococcus porcinus</i> sp. nov. and <i>Enterococcus ratti</i> sp. nov., associated with enteric disorders in animals. <i> Int.J.Syst.Evol.Microbiol. </i><b> 51 </b>: 1737-1743 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/775988/",
        "Enterococcus villorum"
      ],
      "synonyms": null,
      "type_strain": [
        "ATCC 700913",
        "CCUG 43229",
        "DS 1390-83",
        "NCIMB 13634",
        "CIP 107172"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+villorum"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775980/",
      "pnu_no": 775980,
      "label": "Enterococcus pseudoavium",
      "species": "Enterococcus pseudoavium",
      "species_epithet": "pseudoavium",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Collins et al. 1989",
      "taxon": "sp. nov. (VL)",
      "reference": "Int. J. Syst. Bacteriol. 39:371",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-5632.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Collins, M. D., Facklam, R. R., Farrow, J. A. E., Williamson, R. (1989). <i>Enterococcus raffinosus </i>sp. nov., <i>Enterococcus solitarius </i>sp. nov. and <i>Enterococcus pseudoavium</i> sp. nov. <i> FEMS Microbiol.Lett. </i><b> 57 </b>: 283-288 ."
        },
        {
          "pubmed": null,
          "reference": "(1989). Validation of the publication of new names and new combinations previously effectively published outside the IJSB. List No. 30. <i> Int.J.Syst.Bacteriol. </i><b> 39 </b>: 371 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "DSM 5632",
        "NCDO 2138",
        "ATCC 49372",
        "CCUG 33310",
        "CIP 103647",
        "DSMZ 5632",
        "JCM 8732",
        "LMG 11426",
        "NBRC 100491",
        "NCIMB 13084"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+pseudoavium"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775981/",
      "pnu_no": 775981,
      "label": "Enterococcus raffinosus",
      "species": "Enterococcus raffinosus",
      "species_epithet": "raffinosus",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Collins et al. 1989",
      "taxon": "sp. nov. (VL)",
      "reference": "Int. J. Syst. Bacteriol. 39:371",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-5633.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Collins, M. D., Facklam, R. R., Farrow, J. A. E., Williamson, R. (1989). <i>Enterococcus raffinosus </i>sp. nov., <i>Enterococcus solitarius </i>sp. nov. and <i>Enterococcus pseudoavium</i> sp. nov. <i> FEMS Microbiol.Lett. </i><b> 57 </b>: 283-288 ."
        },
        {
          "pubmed": null,
          "reference": "(1989). Validation of the publication of new names and new combinations previously effectively published outside the IJSB. List No. 30. <i> Int.J.Syst.Bacteriol. </i><b> 39 </b>: 371 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "1789/79",
        "DSM 5633",
        "NCTC 12192",
        "ATCC 49427",
        "CCUG 29292",
        "CIP 103329",
        "JCM 8733",
        "LMG 12888",
        "NBRC 100492",
        "strain 1789/79"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+raffinosus"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775982/",
      "pnu_no": 775982,
      "label": "Enterococcus ratti",
      "species": "Enterococcus ratti",
      "species_epithet": "ratti",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Teixeira et al. 2001",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 51:1737*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-15687.html",
      "literature": [
        {
          "pubmed": "11594604",
          "reference": "Teixeira, L. M., Carvalho, M. G. S., Espinola, M. M. B., Steigerwalt, A. G., Douglas, M. P., Brenner, D. J., Facklam, R. R. (2001). <i>Enterococcus porcinus</i> sp. nov. and <i>Enterococcus ratti</i> sp. nov., associated with enteric disorders in animals. <i> Int.J.Syst.Evol.Microbiol. </i><b> 51 </b>: 1737-1743 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "ATCC 700914",
        "CCUG 43228",
        "DS 2705-87",
        "NCIMB 13635",
        "DSM 15687",
        "CIP 107173",
        "NBRC 100698",
        "strain DS 2705-87"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+ratti"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775983/",
      "pnu_no": 775983,
      "label": "Enterococcus saccharolyticus",
      "species": "Enterococcus saccharolyticus",
      "species_epithet": "saccharolyticus",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "(Farrow et al. 1985) Rodrigues and Collins 1991 emend. Chen et al. 2013",
      "taxon": "comb. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 63:4691*",
      "comment": "[DSMZ] emended description: IJSEM 63:4694*",
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-20726.html",
      "literature": [
        {
          "pubmed": "23959830",
          "reference": "Chen, Y. S., Lin, Y. H., Pan, S. F., Ji, S. H., Chang, Y. C., Yu, C. R., Liou, M. S., Wu, H. C., Otoguro, M., Yanagida, F., Liao, C. C., Chiu, C. M., Huang, B. Q. (2013). <i>Enterococcus saccharolyticus</i> subsp. <i>taiwanensis</i> subsp. nov., isolated from broccoli. <i> Int J Syst Evol Microbiol </i><b> 63 </b> ( Pt 12 ): 4691-7 ."
        },
        {
          "pubmed": null,
          "reference": "Rodrigues, U., Collins, M. D. (1990). Phylogenetic analysis of <i>Streptococcus saccharolyticus</i> based on 16S rRNA sequencing. <i> FEMS Microbiol.Lett. </i><b> 71 </b>: 231-234 ."
        },
        {
          "pubmed": null,
          "reference": "Farrow, J. A. E., Kruze, J., Phillips, B. A., Bramley, A. J., Collins, M. D. (1984). Taxonomic studies on <i>Streptococcus bovis </i>and <i>Streptococcus equinus</i>: description of <i>Streptococcus alactolyticus </i>sp. nov and <i>Streptococcus saccharolyticus </i>sp. nov. <i> Syst.Appl.Microbiol. </i><b> 5 </b>: 467-482 ."
        },
        {
          "pubmed": null,
          "reference": "(1991). Validation of the publication of new names and new combinations previously effectively published outside the IJSB. List No. 36. <i> Int.J.Syst.Bacteriol. </i><b> 41 </b>: 178-179 ."
        },
        {
          "pubmed": null,
          "reference": "(1985). Validation of the publication of new names and new combinations previously effectively published outside the IJSB. List No. 17. <i> Int.J.Syst.Bacteriol. </i><b> 35 </b>: 223-225 ."
        }
      ],
      "correct_name": null,
      "synonyms": [
        {
          "synonym_type": "basonym",
          "synonym": "<i>Streptococcus</i> <i>saccharolyticus</i> "
        },
        {
          "synonym_type": "homotypic syn.",
          "synonym": "<i>Enterococcus</i> <i>saccharolyticus</i> subsp. <i>saccharolyticus</i> "
        }
      ],
      "type_strain": [
        "ATCC 43076",
        "DSM 20726",
        "NCDO 2594",
        "CCUG 27643",
        "CCUG 33311",
        "CIP 103246",
        "DSMZ 20726",
        "HAMBI 1576",
        "JCM 8734",
        "LMG 11427",
        "NBRC 100493",
        "NCIMB 702594"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+saccharolyticus"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775984/",
      "pnu_no": 775984,
      "label": "Enterococcus seriolicida",
      "species": "Enterococcus seriolicida",
      "species_epithet": "seriolicida",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Kusuda et al. 1991",
      "taxon": "sp. nov. (VP), heterotypic syn.",
      "reference": "Int. J. Syst. Bacteriol. 41:406*",
      "comment": "[DSMZ] synonymy: IJSB 46:664*",
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-6783.html",
      "literature": [
        {
          "pubmed": "8782673",
          "reference": "Teixeira, L. M., Merquior, V. L. C., Vianni, M. C. E., Carvalho, M. G. S., Fracalanzza, S. E. L., Steigerwalt, A. G., Brenner, D. J., Facklam, R. R. (1996). Phenotypic and genotypic characterization of atypical <i>Lactococcus garvieae</i> strains isolated from water buffalos with subclinical mastitis and confirmation of <i>L</i>. <i>garvieae</i> as a senior subjective synonym of <i>Enterococcus seriolicida</i>. <i> Int.J.Syst.Bacteriol. </i><b> 46 </b>: 664-668 ."
        },
        {
          "pubmed": "1883715",
          "reference": "Kusuda, R., Kawai, K., Salati, F., Banner, C. R., Fryer, J. L. (1991). <i>Enterococcus seriolicida</i> sp. nov., a fish pathogen. <i> Int.J.Syst.Bacteriol. </i><b> 41 </b>: 406-409 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/777418/",
        "Lactococcus garvieae"
      ],
      "synonyms": [
        {
          "synonym_type": "basonym",
          "synonym": "<i>Streptococcus</i> <i>garvieae</i> "
        },
        {
          "synonym_type": "homotypic syn.",
          "synonym": "<i>Lactococcus</i> <i>garvieae</i> subsp. <i>garvieae</i> "
        }
      ],
      "type_strain": [
        "ATCC 49156",
        "DSM 6783",
        "YT-3",
        "CIP 104369",
        "JCM 8735",
        "LMG 12889"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Lactococcus+garvieae"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775985/",
      "pnu_no": 775985,
      "label": "Enterococcus solitarius",
      "species": "Enterococcus solitarius",
      "species_epithet": "solitarius",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Collins et al. 1989",
      "taxon": "sp. nov. (VL)",
      "reference": "Int. J. Syst. Bacteriol. 39:371",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-5634.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Collins, M. D., Facklam, R. R., Farrow, J. A. E., Williamson, R. (1989). <i>Enterococcus raffinosus </i>sp. nov., <i>Enterococcus solitarius </i>sp. nov. and <i>Enterococcus pseudoavium</i> sp. nov. <i> FEMS Microbiol.Lett. </i><b> 57 </b>: 283-288 ."
        },
        {
          "pubmed": null,
          "reference": "(1989). Validation of the publication of new names and new combinations previously effectively published outside the IJSB. List No. 30. <i> Int.J.Syst.Bacteriol. </i><b> 39 </b>: 371 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/782433/",
        "Tetragenococcus solitarius"
      ],
      "synonyms": null,
      "type_strain": [
        "885/78",
        "DSM 5634",
        "NCTC 12193",
        "ATCC 49428",
        "CCUG 29293",
        "CIP 103330",
        "JCM 8736",
        "LMG 12890",
        "NBRC 100494",
        "strain 885/78"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Tetragenococcus+solitarius"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775987/",
      "pnu_no": 775987,
      "label": "Enterococcus sulfureus",
      "species": "Enterococcus sulfureus",
      "species_epithet": "sulfureus",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Martinez-Murcia and Collins 1991",
      "taxon": "sp. nov. (VL)",
      "reference": "Int. J. Syst. Bacteriol. 41:580",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-6905.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Martinez-Murcia, A. J., Collins, M. D. (1991). <i>Enterococcus sulfureus</i>, a new yellow-pigmented <i>Enterococcus</i> species. <i> FEMS Microbiol.Lett. </i><b> 80 </b>: 69-74 ."
        },
        {
          "pubmed": "1742202",
          "reference": "(1991). Validation of the publication of new names and new combinations previously effectively published outside the IJSB. List No. 39. <i> Int.J.Syst.Bacteriol. </i><b> 41 </b>: 580-581 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "DSM 6905",
        "MUTK 31",
        "NCDO 2379",
        "ATCC 49903",
        "CCUG 30571",
        "CCUG 33313",
        "CIP 104373",
        "DSMZ 6905",
        "HAMBI 2232",
        "LMG 13084",
        "NBRC 100680",
        "NCIMB 13117",
        "strain MUTK 31"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+sulfureus"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775988/",
      "pnu_no": 775988,
      "label": "Enterococcus villorum",
      "species": "Enterococcus villorum",
      "species_epithet": "villorum",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Vancanneyt et al. 2001",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 51:393*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": null,
      "literature": [
        {
          "pubmed": "11321084",
          "reference": "Vancanneyt, M., Snauwaert, C., Cleenwerck, I., Baele, M., Descheemaeker, P., Goossens, H., Pot, B., Vandamme, P., Swings, J., Haesebrouck, F., Devriese, L. A. (2001). <i>Enterococcus villorum</i> sp. nov., an enteroadherent bacterium associated with diarrhoea in piglets. <i> Int.J.Syst.Evol.Microbiol. </i><b> 51 </b>: 393-400 ."
        }
      ],
      "correct_name": null,
      "synonyms": [
        {
          "synonym_type": "heterotypic syn.",
          "synonym": "<i>Enterococcus</i> <i>porcinus</i> "
        }
      ],
      "type_strain": [
        "88-5474",
        "CCM 4887",
        "LMG 12287",
        "CCUG 45025",
        "JCM 11557",
        "NBRC 100699",
        "strain 88-5474"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+villorum"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/775989/",
      "pnu_no": 775989,
      "label": "Enterovibrio norvegicus",
      "species": "Enterovibrio norvegicus",
      "species_epithet": "norvegicus",
      "subspecies_epithet": null,
      "genus": "Enterovibrio",
      "familia": "Vibrionaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Thompson et al. 2002",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 52:2015*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterovibrio.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-15893.html",
      "literature": [
        {
          "pubmed": "12508862",
          "reference": "Thompson, F. L., Hoste, B., Thompson, C. C., Goris, J., Gomez-Gil, B., Huys, L., De Vos, P., Swings, J. (2002). <i>Enterovibrio norvegicus</i> gen. nov., sp. nov., isolated from the gut of turbot (<i>Scophthalmus maximus</i>) larvae: a new member of the family <i>Vibrionaceae</i>. <i> Int.J.Syst.Evol.Microbiol. </i><b> 52 </b>: 2015-2022 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "CAIM 430",
        "LMG 19839",
        "DSM 15893",
        "CCUG 47417"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterovibrio+norvegicus"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/777549/",
      "pnu_no": 777549,
      "label": "Leuconostoc mesenteroides",
      "species": "Leuconostoc mesenteroides",
      "species_epithet": "mesenteroides",
      "subspecies_epithet": null,
      "genus": "Leuconostoc",
      "familia": "Leuconostocaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "(Tsenkovskii 1878) van Tieghem 1878",
      "taxon": "comb. nov. (AL)",
      "reference": "Int. J. Syst. Bacteriol. 30:225",
      "comment": null,
      "lpsn": "http://www.bacterio.net/leuconostoc.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-20343.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Garvie, E. I. (1979). Proposal of neotype strains for <i>Leuconostoc mesenteroides</i> (Tsenkovskii) van Tiegham, <i>Leuconostoc dextranicum</i> (beijerinck) Hucker and Peterson, and <i>Leuconostoc cremoris</i> (Knudsen and Sörensen) Garvie. <i> Int.J.Syst.Bacteriol. </i><b> 29 </b>: 149-151 ."
        },
        {
          "pubmed": null,
          "reference": "Tsenkovskii, L. (1878). Gel formation in sugar beet solutions. <i> Proc.Soc.Nat.Sci.Imperial Univ.Kharkov </i><b> 12 </b>: 137-167 ."
        },
        {
          "pubmed": null,
          "reference": "van Tieghem, P. (1878). Sur la gomme du sucerie (Leuconostoc mesenteroides). <i> Ann.Sci.Nat.Bot. </i><b> 7 </b>: 180-203 ."
        }
      ],
      "correct_name": null,
      "synonyms": [
        {
          "synonym_type": "homotypic syn.",
          "synonym": "<i>Leuconostoc</i> <i>mesenteroides</i> subsp. <i>mesenteroides</i> "
        }
      ],
      "type_strain": [
        "DSM 20343",
        "12954",
        "ATCC 8293",
        "CCUG 30066",
        "CIP 102305",
        "DSMZ 20343",
        "HAMBI 2347",
        "JCM 6124",
        "LMG 6893",
        "NBRC 100496",
        "NRRL B-1118",
        "NRRL B-3470",
        "VKM B-1601"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Leuconostoc+mesenteroides"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/777551/",
      "pnu_no": 777551,
      "label": "Leuconostoc mesenteroides subsp. cremoris",
      "species": "Leuconostoc mesenteroides subsp. cremoris",
      "species_epithet": "mesenteroides",
      "subspecies_epithet": "cremoris",
      "genus": "Leuconostoc",
      "familia": "Leuconostocaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "(Knudsen and Sørensen 1929) Garvie 1983",
      "taxon": "comb. nov. (VP)",
      "reference": "Int. J. Syst. Bacteriol. 33:118*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/leuconostoc.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-20346.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Knudsen, S., Sorenson, A. (1929). Beiträge zur Bakteriologie der Säurewecker. Zentralbl. Bakteriol. Parasitenkd. Infektionskr. Hyg. Abt. II. <i> Zentralbl.Bakteriol.Hyg.II Abt. </i><b> 79 </b>: 75-85 ."
        },
        {
          "pubmed": null,
          "reference": "Garvie, E. I. (1983). <i>Leuconostoc mesenteroides</i> subsp.<i> cremoris</i> (Kundsen and Sörensen) comb. nov. and <i>Leuconostoc mesenteroides</i> subsp. <i>dextranicum</i> (Beijerinck) comb. nov. <i> Int.J.Syst.Bacteriol. </i><b> 33 </b>: 118-119 ."
        }
      ],
      "correct_name": null,
      "synonyms": [
        {
          "synonym_type": "basonym",
          "synonym": "<i>Leuconostoc</i> <i>cremoris</i> "
        },
        {
          "synonym_type": "orthographically incorrect name, homotypic syn.",
          "synonym": "<i>Sorenson</i> <i>cremoris</i> "
        }
      ],
      "type_strain": [
        "ATCC 19254",
        "CCM 2078",
        "DSM 20346",
        "IMET 10693",
        "NCDO 543",
        "CCUG 21965",
        "CIP 103009",
        "DSMZ 20346",
        "JCM 16943",
        "LMG 6909",
        "NCIMB 12008",
        "NRRL B-3252",
        "VKM B-1420"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Leuconostoc+mesenteroides+subsp.+cremoris"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/777552/",
      "pnu_no": 777552,
      "label": "Leuconostoc mesenteroides subsp. dextranicum",
      "species": "Leuconostoc mesenteroides subsp. dextranicum",
      "species_epithet": "mesenteroides",
      "subspecies_epithet": "dextranicum",
      "genus": "Leuconostoc",
      "familia": "Leuconostocaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "(Beijerinck 1912) Garvie 1983",
      "taxon": "comb. nov. (VP)",
      "reference": "Int. J. Syst. Bacteriol. 33:118*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/leuconostoc.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-20484.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Beijerinck, M. W. (1912). Mutation bei Mikroben. <i> Folia Microbiol.(Delft) </i><b> 1 </b>: 4-100 ."
        },
        {
          "pubmed": null,
          "reference": "Garvie, E. I. (1983). <i>Leuconostoc mesenteroides</i> subsp.<i> cremoris</i> (Kundsen and Sörensen) comb. nov. and <i>Leuconostoc mesenteroides</i> subsp. <i>dextranicum</i> (Beijerinck) comb. nov. <i> Int.J.Syst.Bacteriol. </i><b> 33 </b>: 118-119 ."
        }
      ],
      "correct_name": null,
      "synonyms": [
        {
          "synonym_type": "basonym",
          "synonym": "<i>Leuconostoc</i> <i>dextranicum</i> "
        }
      ],
      "type_strain": [
        "ATCC 19255",
        "CCM 2086",
        "DSM 20484",
        "NCDO 529",
        "NRRL B-3469",
        "CCUG 21966",
        "CCUG 30065",
        "CIP 102423",
        "DSMZ 20484",
        "JCM 9700",
        "LMG 6908",
        "NBRC 100495",
        "NCAIM B.01658",
        "NCIMB 12007",
        "VKM B-1225"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Leuconostoc+mesenteroides+subsp.+dextranicum"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/777553/",
      "pnu_no": 777553,
      "label": "Leuconostoc mesenteroides subsp. mesenteroides",
      "species": "Leuconostoc mesenteroides subsp. mesenteroides",
      "species_epithet": "mesenteroides",
      "subspecies_epithet": "mesenteroides",
      "genus": "Leuconostoc",
      "familia": "Leuconostocaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "(Tsenkovskii 1878) Garvie 1983",
      "taxon": "comb. nov. (VP), homotypic syn.",
      "reference": "Int. J. Syst. Bacteriol. 33:118*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/leuconostoc.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-20343.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Garvie, E. I. (1979). Proposal of neotype strains for <i>Leuconostoc mesenteroides</i> (Tsenkovskii) van Tiegham, <i>Leuconostoc dextranicum</i> (beijerinck) Hucker and Peterson, and <i>Leuconostoc cremoris</i> (Knudsen and Sörensen) Garvie. <i> Int.J.Syst.Bacteriol. </i><b> 29 </b>: 149-151 ."
        },
        {
          "pubmed": null,
          "reference": "Tsenkovskii, L. (1878). Gel formation in sugar beet solutions. <i> Proc.Soc.Nat.Sci.Imperial Univ.Kharkov </i><b> 12 </b>: 137-167 ."
        },
        {
          "pubmed": null,
          "reference": "van Tieghem, P. (1878). Sur la gomme du sucerie (Leuconostoc mesenteroides). <i> Ann.Sci.Nat.Bot. </i><b> 7 </b>: 180-203 ."
        },
        {
          "pubmed": null,
          "reference": "Garvie, E. I. (1983). <i>Leuconostoc mesenteroides</i> subsp.<i> cremoris</i> (Kundsen and Sörensen) comb. nov. and <i>Leuconostoc mesenteroides</i> subsp. <i>dextranicum</i> (Beijerinck) comb. nov. <i> Int.J.Syst.Bacteriol. </i><b> 33 </b>: 118-119 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/777549/",
        "Leuconostoc mesenteroides"
      ],
      "synonyms": null,
      "type_strain": [
        "ATCC 8293",
        "CCM 1803",
        "DSM 20343",
        "NCDO 523",
        "NCIB 8023",
        "12954",
        "CCUG 30066",
        "CIP 102305",
        "DSMZ 20343",
        "HAMBI 2347",
        "JCM 6124",
        "LMG 6893",
        "NBRC 100496",
        "NRRL B-1118",
        "NRRL B-3470",
        "VKM B-1601"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Leuconostoc+mesenteroides"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/777555/",
      "pnu_no": 777555,
      "label": "Leuconostoc paramesenteroides",
      "species": "Leuconostoc paramesenteroides",
      "species_epithet": "paramesenteroides",
      "subspecies_epithet": null,
      "genus": "Leuconostoc",
      "familia": "Leuconostocaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Garvie 1967",
      "taxon": "species (AL)",
      "reference": "Int. J. Syst. Bacteriol. 30:225",
      "comment": null,
      "lpsn": "http://www.bacterio.net/leuconostoc.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-20288.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Garvie, E. I. (1967). <i>Leuconostoc oenos </i>sp. nov.. <i> J.Gen.Microbiol. </i><b> 48 </b>: 439-447 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/783097/",
        "Weissella paramesenteroides"
      ],
      "synonyms": null,
      "type_strain": [
        "ATCC 33313",
        "DSM 20288",
        "IMET 10704",
        "NCDO 803",
        "CCUG 30068",
        "CIP 102421",
        "JCM 9890",
        "LMG 9852",
        "NCFB 803",
        "NCIMB 13092",
        "NRIC 1542",
        "NRRL B-1186",
        "NRRL B-3471"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Weissella+paramesenteroides"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/777558/",
      "pnu_no": 777558,
      "label": "Leuconostoc pseudomesenteroides",
      "species": "Leuconostoc pseudomesenteroides",
      "species_epithet": "pseudomesenteroides",
      "subspecies_epithet": null,
      "genus": "Leuconostoc",
      "familia": "Leuconostocaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Farrow et al. 1989",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Bacteriol. 39:279*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/leuconostoc.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-20193.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Farrow, J. A. E., Facklam, R. R., Collins, M. D. (1989). Nucleic acid homologies of some vancomycin-resistant leuconostocs and description of <i>Leuconostoc citreum</i> sp. nov. and <i>Leuconostoc pseudomesenteroides</i> sp. nov. <i> Int.J.Syst.Bacteriol. </i><b> 39 </b>: 279-283 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "DSM 20193",
        "NCDO 768",
        "ATCC 12291",
        "CCUG 30063",
        "CIP 103316",
        "DSMZ 20193",
        "JCM 9696",
        "LMG 11482",
        "NCCB 83005",
        "NCIMB 8699"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Leuconostoc+pseudomesenteroides"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/778970/",
      "pnu_no": 778970,
      "label": "Oerskovia enterophila",
      "species": "Oerskovia enterophila",
      "species_epithet": "enterophila",
      "subspecies_epithet": null,
      "genus": "Oerskovia",
      "familia": "Promicromonosporaceae",
      "classis": "Actinobacteria",
      "phylum": "Actinobacteria",
      "regio": "Bacteria",
      "authors": "(Jáger et al. 1983) Stackebrandt et al. 2002",
      "taxon": "comb. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 52:1105*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/oerskovia.html",
      "wink_compendium": "http://www.dsmz.de/microorganisms/wink_pdf/DSM43852.pdf",
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-43852.html",
      "literature": [
        {
          "pubmed": "12148614",
          "reference": "Stackebrandt, E., Breymann, S., Steiner, U., Prauser, H., Weiss, N., Schumann, P. (2002). Re-evaluation of the status of the genus <i>Oerskovia</i>, reclassification of <i>Promicromonospora enterophila</i> (Jager <i>et al</i>. 1983) as <i>Oerskovia enterophila</i> comb. nov. and description of <i>Oerskovia jenensis</i> sp. nov. and <i>Oerskovia paurometabola</i> sp. nov. <i> Int.J.Syst.Evol.Microbiol. </i><b> 52 </b>: 1105-1111 ."
        },
        {
          "pubmed": null,
          "reference": "Jager, K., Màrialigeti, K., Hauck, M., Barabas, G. (1983). <i>Promicromonospora</i> <i>enterophila</i> sp. nov., a new species of monospore actinomycetes. <i> Int.J.Syst.Bacteriol. </i><b> 33 </b>: 525-531 ."
        }
      ],
      "correct_name": null,
      "synonyms": [
        {
          "synonym_type": "basonym",
          "synonym": "<i>Promicromonospora</i> <i>enterophila</i> "
        }
      ],
      "type_strain": [
        "ATCC 35307",
        "DFA-19",
        "DSM 43852",
        "HMGB B1078",
        "IMET 7687",
        "JCM 7350",
        "HMGB B 1078",
        "IFO 14295",
        "NBRC 14295",
        "NRRL B-16223"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Oerskovia+enterophila"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/779811/",
      "pnu_no": 779811,
      "label": "Promicromonospora enterophila",
      "species": "Promicromonospora enterophila",
      "species_epithet": "enterophila",
      "subspecies_epithet": null,
      "genus": "Promicromonospora",
      "familia": "Promicromonosporaceae",
      "classis": "Actinobacteria",
      "phylum": "Actinobacteria",
      "regio": "Bacteria",
      "authors": "Jáger et al. 1983",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Bacteriol. 33:525*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/promicromonospora.html",
      "wink_compendium": "http://www.dsmz.de/microorganisms/wink_pdf/DSM43852.pdf",
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-43852.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Jager, K., Màrialigeti, K., Hauck, M., Barabas, G. (1983). <i>Promicromonospora</i> <i>enterophila</i> sp. nov., a new species of monospore actinomycetes. <i> Int.J.Syst.Bacteriol. </i><b> 33 </b>: 525-531 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/778970/",
        "Oerskovia enterophila"
      ],
      "synonyms": null,
      "type_strain": [
        "DFA-19",
        "DSM 43852",
        "HMGB B1078",
        "IMET 7687",
        "ATCC 35307",
        "HMGB B 1078",
        "IFO 14295",
        "JCM 7350",
        "NBRC 14295",
        "NRRL B-16223"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Oerskovia+enterophila"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/783097/",
      "pnu_no": 783097,
      "label": "Weissella paramesenteroides",
      "species": "Weissella paramesenteroides",
      "species_epithet": "paramesenteroides",
      "subspecies_epithet": null,
      "genus": "Weissella",
      "familia": "Leuconostocaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "(Garvie 1967) Collins et al. 1994",
      "taxon": "comb. nov. (VL)",
      "reference": "Int. J. Syst. Bacteriol. 44:370",
      "comment": null,
      "lpsn": "http://www.bacterio.net/weissella.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-20288.html",
      "literature": [
        {
          "pubmed": "8294308",
          "reference": "Collins, M. D., Samelis, J., Metaxopoulos, J., Wallbanks, S. (1993). Taxonomic studies on some leuconostoc-like organisms from fermented sausages: description of a new genus <i>Weissella</i> for the <i>Leuconostoc paramesenteroides</i> group of species. <i> J.Appl.Bacteriol. </i><b> 75 </b>: 595-603 ."
        },
        {
          "pubmed": null,
          "reference": "Garvie, E. I. (1967). <i>Leuconostoc oenos </i>sp. nov.. <i> J.Gen.Microbiol. </i><b> 48 </b>: 439-447 ."
        },
        {
          "pubmed": null,
          "reference": "(1994). Validation of the publication of new names and new combinations previously effectively published outside the IJSB. List No. 49. <i> Int.J.Syst.Bacteriol. </i><b> 44 </b>: 370-371 ."
        }
      ],
      "correct_name": null,
      "synonyms": [
        {
          "synonym_type": "basonym",
          "synonym": "<i>Leuconostoc</i> <i>paramesenteroides</i> "
        }
      ],
      "type_strain": [
        "ATCC 33313",
        "DSM 20288",
        "IMET 10704",
        "NCDO 803",
        "CCUG 30068",
        "CIP 102421",
        "JCM 9890",
        "LMG 9852",
        "NCFB 803",
        "NCIMB 13092",
        "NRIC 1542",
        "NRRL B-1186",
        "NRRL B-3471"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Weissella+paramesenteroides"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/783199/",
      "pnu_no": 783199,
      "label": "Yersinia enterocolitica subsp. enterocolitica",
      "species": "Yersinia enterocolitica subsp. enterocolitica",
      "species_epithet": "enterocolitica",
      "subspecies_epithet": "enterocolitica",
      "genus": "Yersinia",
      "familia": "Yersiniaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "(Schleifstein and Coleman 1939) Neubauer et al. 2000",
      "taxon": "comb. nov. (VL), homotypic syn.",
      "reference": "Int. J. Syst. Evol. Microbiol. 50:1415",
      "comment": null,
      "lpsn": "http://www.bacterio.net/yersinia.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-4780.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Frederiksen, W., (1964). Proc. XIV Scad. Congr. Pathol. Microbiol. pp. 103-104. Norw. Univ. Press."
        },
        {
          "pubmed": "844324",
          "reference": "Bottone, E. J. (1977). <i>Yersinia enterocolitica</i>: a panoramic view of a charismatic microorganism. <i> CRC Crit.Rev.Microbiol. </i><b> 5 </b>: 211-241 ."
        },
        {
          "pubmed": "11043982",
          "reference": "Neubauer, H., Aleksic, S., Hensel, A., Finke, E. J., Meyer, H. (2000). <i>Yersinia enterocolitica</i> 16S rRNA gene types belong to the same genospecies but form three homology groups. <i> Int.J.Med.Microbiol. </i><b> 290 </b>: 61-64 ."
        },
        {
          "pubmed": null,
          "reference": "Schleifstein, J. I., Coleman, M. B. (1939). An unidentified microorganism resembling <i>B. lignieri</i> and <i>Past. pseudotuberculosis</i>, and pathogenic for man. <i> N.Y.State J.Med. </i><b> 39 </b>: 1749-1753 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/785221/",
        "Yersinia enterocolitica"
      ],
      "synonyms": null,
      "type_strain": [
        "ATCC 9610",
        "DSM 4780",
        "CCUG 11291",
        "CCUG 12369",
        "CIP 80-27",
        "JCM 7577",
        "LMG 7899",
        "NCTC 12982"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Yersinia+enterocolitica"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/783200/",
      "pnu_no": 783200,
      "label": "Yersinia enterocolitica subsp. palearctica",
      "species": "Yersinia enterocolitica subsp. palearctica",
      "species_epithet": "enterocolitica",
      "subspecies_epithet": "palearctica",
      "genus": "Yersinia",
      "familia": "Yersiniaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Neubauer et al. 2000",
      "taxon": "subsp. nov. (VL)",
      "reference": "Int. J. Syst. Evol. Microbiol. 50:1415",
      "comment": null,
      "lpsn": "http://www.bacterio.net/yersinia.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-13030.html",
      "literature": [
        {
          "pubmed": "11043982",
          "reference": "Neubauer, H., Aleksic, S., Hensel, A., Finke, E. J., Meyer, H. (2000). <i>Yersinia enterocolitica</i> 16S rRNA gene types belong to the same genospecies but form three homology groups. <i> Int.J.Med.Microbiol. </i><b> 290 </b>: 61-64 ."
        },
        {
          "pubmed": "10939643",
          "reference": "(2000). Validation of publication of new names and new combinations previously effectively published outside the IJSEM. List No. 75. <i> Int.J.Syst.Evol.Microbiol. </i><b> 50 </b>: 1415-1417 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "DSM 13030",
        "Y11",
        "CIP 106945"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Yersinia+enterocolitica+subsp.+palearctica"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/783768/",
      "pnu_no": 783768,
      "label": "Enterobacter hormaechei",
      "species": "Enterobacter hormaechei",
      "species_epithet": "hormaechei",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "O'Hara et al. 1990 emend. Hoffmann et al. 2005",
      "taxon": "sp. nov. (VL)",
      "reference": "Int. J. Syst. Bacteriol. 40:105",
      "comment": "[DSMZ] emended description: IJSEM 67:7 (List of Changes in Taxonomic Opinion) // [IJSEM] Not Ou02019Hara et al. 1989. Syllabification and etymology must be (hor.maeu02019che.i. N.L. gen. n. hormaechei after Estenio Hormaecheu02026).",
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-12409.html",
      "literature": [
        {
          "pubmed": "2778068",
          "reference": "O'Hara, C. M., Steigerwalt, A. G., Hill, B. C., Farmer, J. J., Fanning, G. R., Brenner, D. J. (1989). <i>Enterobacter hormaechei</i>, a new species of the family <i>Enterobacteriaceae</i> formerly known as Enteric Group 75. <i> J.Clin.Microbiol. </i><b> 27 </b>: 2046-2049 ."
        },
        {
          "pubmed": null,
          "reference": "(1990). Validation of the publication of new names and new combinations previously effectively published outside the IJSB. List No. 32. <i> Int.J.Syst.Bacteriol. </i><b> 40 </b>: 105-106 ."
        }
      ],
      "correct_name": null,
      "synonyms": [
        {
          "synonym_type": "homotypic syn.",
          "synonym": "<i>Enterobacter</i> <i>hormaechei</i> subsp. <i>hormaechei</i> "
        }
      ],
      "type_strain": [
        "0992-77",
        "ATCC 49162",
        "DSM 12409",
        "CCUG 27126",
        "CIP 103441",
        "0992-77; ATCC 49162; CIP 103441; CCUG 27126"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterobacter+hormaechei"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/783769/",
      "pnu_no": 783769,
      "label": "Enterobacter intermedium",
      "species": "Enterobacter intermedium",
      "species_epithet": "intermedium",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Izard et al. 1980",
      "taxon": "orthographically incorrect name",
      "reference": "Int. J. Syst. Bacteriol. 30:601",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-4581.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "Izard, D. F., Gavini, F., Leclerc, H. (1980). Polynucleotide sequence relatedness and genome size among <i>Enterobacter intermedium</i> sp. nov. and the species <i>Enterobacter cloacae</i> and <i>Klebsiella pneumoniae</i>. <i> Zbl.Bakt.Hyg., I.Abt.Orig.C </i><b> 1 </b>: 51-60 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/777172/",
        "Kluyvera intermedia"
      ],
      "synonyms": [
        {
          "synonym_type": "basonym",
          "synonym": "<i>Enterobacter</i> <i>intermedius</i> "
        },
        {
          "synonym_type": "heterotypic syn.",
          "synonym": "<i>Kluyvera</i> <i>cochleae</i> "
        }
      ],
      "type_strain": [
        "ATCC 33110",
        "CCUG 14183",
        "CIP 79-27",
        "CUETM 77-130",
        "DSM 4581",
        "Gavini E 86",
        "HAMBI 1299",
        "JCM 1238",
        "LMG 2785",
        "NBRC 102594",
        "NCTC 12125"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Kluyvera+intermedia"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/783770/",
      "pnu_no": 783770,
      "label": "Enterobacter nimipressuralis",
      "species": "Enterobacter nimipressuralis",
      "species_epithet": "nimipressuralis",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "(Carter 1945) Brenner et al. 1988",
      "taxon": "comb. nov. (VL), homotypic syn.",
      "reference": "Int. J. Syst. Bacteriol. 38:220",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-18955.html",
      "literature": [
        {
          "pubmed": "3711302",
          "reference": "Brenner, D. J., McWhorter, A. C., Kai, A., Steigerwalt, A. G., Farmer, J. J. (1986). <i>Enterobacter asburiae</i> sp. nov., a new species found in clinical specimens, and reassignement of <i>Erwinia dissolvens</i> and <i>Erwinia nimipressuralis</i> to the genus <i>Enterobacter</i> as <i>Enterobacter dissolvens</i> comb. nov. and <i>Enterobacter nimipressuralis</i> comb. nov. <i> J.Clin.Microbiol. </i><b> 23 </b>: 1114-1120 ."
        },
        {
          "pubmed": null,
          "reference": "(1988). Validation of the publication of new names and new combinations previously effectively published outside the IJSB. List No. 25. <i> Int.J.Syst.Bacteriol. </i><b> 38 </b>: 220-222 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/791219/",
        "Lelliottia nimipressuralis"
      ],
      "synonyms": [
        {
          "synonym_type": "basonym",
          "synonym": "<i>Erwinia</i> <i>nimipressuralis</i> "
        }
      ],
      "type_strain": [
        "ATCC 9912",
        "CIP 104980",
        "DSM 18955",
        "ICMP 1577",
        "JCM 6050",
        "NCPPB 2045"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Lelliottia+nimipressuralis"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/783771/",
      "pnu_no": 783771,
      "label": "Enterobacter taylorae",
      "species": "Enterobacter taylorae",
      "species_epithet": "taylorae",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Farmer et al. 1985",
      "taxon": "sp. nov. (VL), heterotypic syn.",
      "reference": "Int. J. Syst. Bacteriol. 35:223",
      "comment": "[DSMZ] synonymy: Res. Microbiol. 140:459 (1989); IJSB 44:586*",
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-17580.html",
      "literature": [
        {
          "pubmed": "3968204",
          "reference": "Farmer, J. J., Fanning, G. R., Davis, B. R., O'Hara, M., Riddle, C., Hickman-Brenner, F. W., Asbury, M. A., Lowery, V. A., Brenner, D. J. (1985). <i>Escherichia fergusonii</i> and <i>Enterobacter taylorae</i>, two new species of <i>Enterobacteriaceae</i> isolated from clinical specimens. <i> J.Clin.Microbiol. </i><b> 21 </b>: 77-81 ."
        },
        {
          "pubmed": null,
          "reference": "(1985). Validation of the publication of new names and new combinations previously effectively published outside the IJSB. List No. 17. <i> Int.J.Syst.Bacteriol. </i><b> 35 </b>: 223-225 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/775932/",
        "Enterobacter cancerogenus"
      ],
      "synonyms": [
        {
          "synonym_type": "basonym",
          "synonym": "<i>Erwinia</i> <i>cancerogena</i> "
        }
      ],
      "type_strain": [
        "ATCC 35317",
        "CDC 2126-81",
        "DSM 17580",
        "CCUG 18765",
        "CCUG 25589",
        "JCM 3943",
        "NCTC 12126"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterobacter+cancerogenus"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/783772/",
      "pnu_no": 783772,
      "label": "Enterococcus caccae",
      "species": "Enterococcus caccae",
      "species_epithet": "caccae",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Carvalho et al. 2006",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 56:1505*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-19114.html",
      "literature": [
        {
          "pubmed": "16825620",
          "reference": "Carvalho, M. d., Shewmaker, P. L., Steigerwalt, A. G., Morey, R. E., Sampson, A. J., Joyce, K., Barrett, T. J., Teixeira, L. M., Facklam, R. R. (2006). <i>Enterococcus caccae</i> sp. nov., isolated from human stools. <i> Int.J.Syst.Evol.Microbiol. </i><b> 56 </b>: 1505-1508 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "2215-02",
        "ATCC BAA-1240",
        "CCUG 51564",
        "SS-1777",
        "DSM 19114"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+caccae"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/783773/",
      "pnu_no": 783773,
      "label": "Enterococcus canintestini",
      "species": "Enterococcus canintestini",
      "species_epithet": "canintestini",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Naser et al. 2005",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 55:2177*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-21207.html",
      "literature": [
        {
          "pubmed": "16166728",
          "reference": "Naser, S. M., Vancanneyt, M., De Graef, E., Devriese, L. A., Snauwaert, C., Lefebvre, K., Hoste, B., Svec, P., Decostere, A., Haesebrouck, F., Swings, J. (2005). <i>Enterococcus canintestini</i> sp. nov., from faecal samples of healthy dogs. <i> Int.J.Syst.Evol.Microbiol. </i><b> 55 </b>: 2177-2182 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "CCM 7285",
        "LMG 13590",
        "DSM 21207",
        "CCUG 37857",
        "CCUG 51312"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+canintestini"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/783774/",
      "pnu_no": 783774,
      "label": "Enterococcus devriesei",
      "species": "Enterococcus devriesei",
      "species_epithet": "devriesei",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "&#x0160;vec et al. 2005",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 55:2479*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-22802.html",
      "literature": [
        {
          "pubmed": "16280513",
          "reference": "Svec, P., Vancanneyt, M., Koort, J., Naser, S. M., Hoste, B., Vihavainen, E., Vandamme, P., Swings, J., Björkroth, J. (2005). <i>Enterococcus devriesei</i> sp. nov., associated with animal sources. <i> Int.J.Syst.Evol.Microbiol. </i><b> 55 </b>: 2479-2484 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "CCM 7299",
        "LMG 14595",
        "DSM 22802",
        "CCUG 37865"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+devriesei"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/783775/",
      "pnu_no": 783775,
      "label": "Enterococcus saccharominimus",
      "species": "Enterococcus saccharominimus",
      "species_epithet": "saccharominimus",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Vancanneyt et al. 2004",
      "taxon": "sp. nov. (VP), heterotypic syn.",
      "reference": "Int. J. Syst. Evol. Microbiol. 54:2175*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": null,
      "literature": [
        {
          "pubmed": "16449449",
          "reference": "Naser, S. M., Vancanneyt, M., Hoste, B., Snauwaert, C., Vandemeulebroecke, K., Swings, J. (2006). Reclassification of <i>Enterococcus flavescens</i> Pompei et al. 1992 as a later synonym of <i>Enterococcus casseliflavus</i> (ex Vaughan et al. 1979) Collins et al. 1984 and <i>Enterococcus saccharominimus</i> Vancanneyt et al. 2004 as a later synonym of <i>Enterococcus italicus</i> Fortina et al. 2004. <i> Int.J.Syst.Evol.Microbiol. </i><b> 56 </b>: 413-416 ."
        },
        {
          "pubmed": "15545454",
          "reference": "Vancanneyt, M., Zamfir, M., Devriese, L. A., Lefebvre, K., Engelbeen, K., Vandermeulebroecke, K., Amar, M., De Vuyst, L., Haesebrouck, F., Swings, J. (2004). <i>Enterococcus saccharominimus</i> sp. nov., from dairy products. <i> Int.J.Syst.Evol.Microbiol. </i><b> 54 </b>: 2175-2179 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/775973/",
        "Enterococcus italicus"
      ],
      "synonyms": null,
      "type_strain": [
        "CCM 7220",
        "LMG 21727"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+italicus"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/783776/",
      "pnu_no": 783776,
      "label": "Enterococcus silesiacus",
      "species": "Enterococcus silesiacus",
      "species_epithet": "silesiacus",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "&#x0160;vec et al. 2006",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 56:577*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-22801.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "(1943). Forty-fourth General Meeting of the Society of American Bacteriologists. (Scientific Proceedings). <i> J.Bacteriol. </i><b> 45 </b>: 11-35 ."
        },
        {
          "pubmed": "16514030",
          "reference": "Svec, P., Vancanneyt, M., Sedlácek, I., Naser, S. M., Snauwaert, C., Lefebvre, K., Hoste, B., Swings, J. (2006). <i>Enterococcus silesiacus</i> sp. nov. and <i>Enterococcus termitis</i> sp. nov. <i> Int.J.Syst.Evol.Microbiol. </i><b> 56 </b>: 577-581 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "CCM 7319",
        "LMG 23085",
        "W442",
        "DSM 22801",
        "strain W442"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+silesiacus"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/783777/",
      "pnu_no": 783777,
      "label": "Enterococcus termitis",
      "species": "Enterococcus termitis",
      "species_epithet": "termitis",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "&#x0160;vec et al. 2006",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 56:577*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-22803.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "(1943). Forty-fourth General Meeting of the Society of American Bacteriologists. (Scientific Proceedings). <i> J.Bacteriol. </i><b> 45 </b>: 11-35 ."
        },
        {
          "pubmed": "16514030",
          "reference": "Svec, P., Vancanneyt, M., Sedlácek, I., Naser, S. M., Snauwaert, C., Lefebvre, K., Hoste, B., Swings, J. (2006). <i>Enterococcus silesiacus</i> sp. nov. and <i>Enterococcus termitis</i> sp. nov. <i> Int.J.Syst.Evol.Microbiol. </i><b> 56 </b>: 577-581 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "CCM 7300",
        "LMG 8895",
        "DSM 22803"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+termitis"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/783778/",
      "pnu_no": 783778,
      "label": "Enterovibrio coralii",
      "species": "Enterovibrio coralii",
      "species_epithet": "coralii",
      "subspecies_epithet": null,
      "genus": "Enterovibrio",
      "familia": "Vibrionaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Thompson et al. 2005 emend. Liu et al. 2016",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 55:913*",
      "comment": "[DSMZ] emended description: IJSEM 66:323*",
      "lpsn": "http://www.bacterio.net/enterovibrio.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-19135.html",
      "literature": [
        {
          "pubmed": "15774685",
          "reference": "Thompson, F. L., Thompson, C. C., Naser, S., Hoste, B., Vandermeulebroecke, K., Munn, C., Bourne, D., Swings, J. (2005). <i>Photobacterium rosenbergii</i> sp. nov. and <i>Enterovibrio coralii</i> sp. nov., vibrios associated with coral bleaching. <i> Int.J.Syst.Evol.Microbiol. </i><b> 55 </b>: 913-917 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "CBMAI 623",
        "CC17",
        "LMG 22228",
        "DSM 19135"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterovibrio+coralii"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/785221/",
      "pnu_no": 785221,
      "label": "Yersinia enterocolitica",
      "species": "Yersinia enterocolitica",
      "species_epithet": "enterocolitica",
      "subspecies_epithet": null,
      "genus": "Yersinia",
      "familia": "Yersiniaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "(Schleifstein and Coleman 1939) Frederiksen 1964",
      "taxon": "comb. nov. (AL)",
      "reference": "Int. J. Syst. Bacteriol. 30:225",
      "comment": null,
      "lpsn": "http://www.bacterio.net/yersinia.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-4780.html",
      "literature": null,
      "correct_name": null,
      "synonyms": [
        {
          "synonym_type": "homotypic syn.",
          "synonym": "<i>Yersinia</i> <i>enterocolitica</i> subsp. <i>enterocolitica</i> "
        }
      ],
      "type_strain": [
        "ATCC 9610",
        "CCUG 11291",
        "CCUG 12369",
        "CIP 80-27",
        "DSM 4780",
        "JCM 7577",
        "LMG 7899",
        "NCTC 12982"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Yersinia+enterocolitica"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/786077/",
      "pnu_no": 786077,
      "label": "Enterobacter pulveris",
      "species": "Enterobacter pulveris",
      "species_epithet": "pulveris",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Stephan et al. 2008",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 58:237*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-19144.html",
      "literature": [
        {
          "pubmed": "18175715",
          "reference": "Stephan, R., Van, T. S., Cleenwerck, I., Iversen, C., Joosten, H., De, V. P., Lehner, A. (2008). <i>Enterobacter pulveris</i> sp. nov., isolated from fruit powder, infant formula and an infant formula production environment. <i> Int J Syst Evol Microbiol </i><b> 58 </b> ( Pt 1 ): 237-241 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/792221/",
        "Franconibacter pulveris"
      ],
      "synonyms": [
        {
          "synonym_type": "homotypic syn.",
          "synonym": "<i>Cronobacter</i> <i>pulveris</i> "
        }
      ],
      "type_strain": [
        "601/05",
        "DSM 19144",
        "LMG 24057",
        "JCM 16471"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Franconibacter+pulveris"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/786700/",
      "pnu_no": 786700,
      "label": "Enterococcus camelliae",
      "species": "Enterococcus camelliae",
      "species_epithet": "camelliae",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Sukontasing et al. 2007",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 57:2151*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": null,
      "literature": [
        {
          "pubmed": "17766890",
          "reference": "Sukontasing, S., Tanasupawat, S., Moonmangmee, S., Lee, J. S., Suzuki, K. (2007). <i>Enterococcus camelliae</i> sp. nov., isolated from fermented tea leaves in Thailand. <i> Int.J.Syst.Evol.Microbiol. </i><b> 57 </b>: 2151-2154 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "FP15-1",
        "KCTC 13133",
        "NBRC 101868",
        "NRIC 0105",
        "TISTR 932",
        "PCU 277"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+camelliae"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/787438/",
      "pnu_no": 787438,
      "label": "Enterococcus thailandicus",
      "species": "Enterococcus thailandicus",
      "species_epithet": "thailandicus",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Tanasupawat et al. 2008",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 58:1630*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-21767.html",
      "literature": [
        {
          "pubmed": "18599707",
          "reference": "Tanasupawat, S., Sukontasing, S., Lee, J. S. (2008). <i>Enterococcus thailandicus</i> sp. nov., isolated from fermented sausage ('mum') in Thailand. <i> Int J Syst Evol Microbiol </i><b> 58 </b> ( 7 ): 1630-1634 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "FP48-3 TISTR 933",
        "KCTC 13134",
        "NBRC 101867",
        "NRIC 0107",
        "PCU 282",
        "TISTR 933",
        "DSM 21767",
        "FP48-3"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+thailandicus"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/787768/",
      "pnu_no": 787768,
      "label": "Enterovibrio calviensis",
      "species": "Enterovibrio calviensis",
      "species_epithet": "calviensis",
      "subspecies_epithet": null,
      "genus": "Enterovibrio",
      "familia": "Vibrionaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "(Denner et al. 2002) Pascual et al. 2009",
      "taxon": "comb. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 59:698*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterovibrio.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-14347.html",
      "literature": [
        {
          "pubmed": "19329591",
          "reference": "Pascual, J., Macián, M. C., Arahal, D. R., Garay, E., Pujalte, M. J. (2009). Description of <i>Enterovibrio nigricans</i> sp. nov., reclassification of <i>Vibrio calviensis</i> as <i>Enterovibrio calviensis </i>comb. nov. and emended description of the genus <i>Enterovibrio</i> Thompson et al. 2002. <i> Int J Syst Evol Microbiol </i><b> 59 </b> ( Pt 4 ): 698-704 ."
        },
        {
          "pubmed": "11931167",
          "reference": "Denner, E. B. M., Vybiral, D., Fischer, U. R., Velimirov, B., Busse, H. J. (2002). <i>Vibrio calviensis</i> sp. nov., a halophilic, facultatively oligotrophic 0.2 micrometre-filterable marine bacterium. <i> Int.J.Syst.Evol.Microbiol. </i><b> 52 </b>: 549-553 ."
        }
      ],
      "correct_name": null,
      "synonyms": [
        {
          "synonym_type": "basonym",
          "synonym": "<i>Vibrio</i> <i>calviensis</i> "
        }
      ],
      "type_strain": [
        "RE35F/12",
        "DSM 14347",
        "CIP 107077",
        "CECT 7414",
        "CCUG 48319 B",
        "ATCC BAA-606",
        "CCUG 48319",
        "RE35/F12"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterovibrio+calviensis"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/787780/",
      "pnu_no": 787780,
      "label": "Enterovibrio nigricans",
      "species": "Enterovibrio nigricans",
      "species_epithet": "nigricans",
      "subspecies_epithet": null,
      "genus": "Enterovibrio",
      "familia": "Vibrionaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Pascual et al. 2009",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 59:698*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterovibrio.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-22720.html",
      "literature": [
        {
          "pubmed": "19329591",
          "reference": "Pascual, J., Macián, M. C., Arahal, D. R., Garay, E., Pujalte, M. J. (2009). Description of <i>Enterovibrio nigricans</i> sp. nov., reclassification of <i>Vibrio calviensis</i> as <i>Enterovibrio calviensis </i>comb. nov. and emended description of the genus <i>Enterovibrio</i> Thompson et al. 2002. <i> Int J Syst Evol Microbiol </i><b> 59 </b> ( Pt 4 ): 698-704 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "DAl 1-1-5",
        "CAIM 661",
        "CECT 7320",
        "DSM 22720",
        "strain DAl 1-1-5"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterovibrio+nigricans"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/787976/",
      "pnu_no": 787976,
      "label": "Enterorhabdus mucosicola",
      "species": "Enterorhabdus mucosicola",
      "species_epithet": "mucosicola",
      "subspecies_epithet": null,
      "genus": "Enterorhabdus",
      "familia": "Eggerthellaceae",
      "classis": "Coriobacteriia",
      "phylum": "Actinobacteria",
      "regio": "Bacteria",
      "authors": "Clavel et al. 2009",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 59:1805*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterorhabdus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-19490.html",
      "literature": [
        {
          "pubmed": "19542111",
          "reference": "Clavel, T., Charrier, C., Braune, A., Wenning, M., Blaut, M., Haller, D. (2009). Isolation of bacteria from the ileal mucosa of TNF<sup>deltaARE</sup> mice and description of <i>Enterorhabdus mucosicola</i> gen. nov., sp. nov.. <i> Int J Syst Evol Microbiol </i><b> 59 </b> ( Pt 7 ): 1805-1812 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/798329/",
        "Adlercreutzia mucosicola"
      ],
      "synonyms": null,
      "type_strain": [
        "Mt1B8",
        "DSM 19490",
        "CCUG 54980"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Adlercreutzia+mucosicola"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/788002/",
      "pnu_no": 788002,
      "label": "Enterobacter oryzae",
      "species": "Enterobacter oryzae",
      "species_epithet": "oryzae",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Peng et al. 2009",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 59:1650*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": null,
      "literature": [
        {
          "pubmed": "19578150",
          "reference": "Peng, G., Zhang, W., Luo, H., Xie, H., Lai, W., Tan, Z. (2009). <i>Enterobacter oryzae</i> sp. nov., a nitrogen-fixing bacterium isolated from the wild rice species <i>Oryza latifolia</i>. <i> Int J Syst Evol Microbiol </i><b> 59 </b> ( Pt 7 ): 1650-1655 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/791225/",
        "Kosakonia oryzae"
      ],
      "synonyms": null,
      "type_strain": [
        "Ola 51",
        "CGMCC 1.7012",
        "LMG 24251"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Kosakonia+oryzae"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/788612/",
      "pnu_no": 788612,
      "label": "Enterorhabdus caecimuris",
      "species": "Enterorhabdus caecimuris",
      "species_epithet": "caecimuris",
      "subspecies_epithet": null,
      "genus": "Enterorhabdus",
      "familia": "Eggerthellaceae",
      "classis": "Coriobacteriia",
      "phylum": "Actinobacteria",
      "regio": "Bacteria",
      "authors": "Clavel et al. 2010",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 60:1527*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterorhabdus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-21839.html",
      "literature": [
        {
          "pubmed": "19684311",
          "reference": "Clavel, T., Duck, W., Charrier, C., Wenning, M., Elson, C., Haller, D. (2010). <i>Enterorhabdus caecimuris</i> sp. nov., a member of the family <i>Coriobacteriaceae</i> isolated from a mouse model of spontaneous colitis, and emended description of the genus <i>Enterorhabdus</i> Clavel <i>et al</i>. 2009. <i> Int J Syst Evol Microbiol </i><b> 60 </b> ( Pt 7 ): 1527-1531 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/798328/",
        "Adlercreutzia caecimuris"
      ],
      "synonyms": null,
      "type_strain": [
        "B7",
        "DSM 21839",
        "CCUG 56815"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Adlercreutzia+caecimuris"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/788636/",
      "pnu_no": 788636,
      "label": "Enterobacter arachidis",
      "species": "Enterobacter arachidis",
      "species_epithet": "arachidis",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Madhaiyan et al. 2010",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 60:1559*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-25165.html",
      "literature": [
        {
          "pubmed": "19684326",
          "reference": "Madhaiyan, M., Poonguzhali, S., Lee, J. S., Saravanan, V. S., Lee, K. C., Santhanakrishnan, P. (2010). <i>Enterobacter arachidis</i> sp. nov., a plant-growth-promoting diazotrophic bacterium isolated from rhizosphere soil of groundnut. <i> Int J Syst Evol Microbiol </i><b> 60 </b> ( Pt 7 ): 1559-1564 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/791226/",
        "Kosakonia arachidis"
      ],
      "synonyms": null,
      "type_strain": [
        "Ah-143",
        "KCTC 22375",
        "NCIMB 14469",
        "DSM 25165"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Kosakonia+arachidis"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/789236/",
      "pnu_no": 789236,
      "label": "Enterobacter soli",
      "species": "Enterobacter soli",
      "species_epithet": "soli",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Manter et al. 2011",
      "taxon": "sp. nov. (VL)",
      "reference": "Int. J. Syst. Evol. Microbiol. 61:1499",
      "comment": "[IJSEM] The culture collection accession number NRRL B-59409 is also cited in the effective publication, but the authors did not provide evidence that the type strain is deposited in this collection.",
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": null,
      "literature": [
        {
          "pubmed": "21742853",
          "reference": "(2011). List of new names and new combinations previously effectively, but not validly, published. <i> Int J Syst Evol Microbiol </i><b> 61 </b> ( Pt 7 ): 1499-1501 ."
        },
        {
          "pubmed": "21104086",
          "reference": "Manter, D. K., Hunter, W. J., Vivanco, J. M. (2011). <i>Enterobacter soli</i> sp. nov.: a lignin-degrading gamma-proteobacteria isolated from soil. <i> Curr Microbiol </i><b> 62 </b> ( 3 ): 1044-1049 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "LF7",
        "ATCC BAA-2102",
        "LMG 25861",
        "NRRL B-59409"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterobacter+soli"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/789237/",
      "pnu_no": 789237,
      "label": "Enterococcus viikkiensis",
      "species": "Enterococcus viikkiensis",
      "species_epithet": "viikkiensis",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Rahkila et al. 2011",
      "taxon": "sp. nov. (VL)",
      "reference": "Int. J. Syst. Evol. Microbiol. 61:1499",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-24043.html",
      "literature": [
        {
          "pubmed": "21742853",
          "reference": "(2011). List of new names and new combinations previously effectively, but not validly, published. <i> Int J Syst Evol Microbiol </i><b> 61 </b> ( Pt 7 ): 1499-1501 ."
        },
        {
          "pubmed": "21183650",
          "reference": "Rahkila, R., Johansson, P., Säde, E., Björkroth, J. (2011). Identification of enterococci from broiler products and a broiler processing plant and description of<i> Enterococcus viikkiensis</i> sp. nov.. <i> Appl Environ Microbiol </i><b> 77 </b> ( 4 ): 1196-1203 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "DSM 24043",
        "LMG 26075",
        "IE3.2"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+viikkiensis"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/789537/",
      "pnu_no": 789537,
      "label": "Enterobacter mori",
      "species": "Enterobacter mori",
      "species_epithet": "mori",
      "subspecies_epithet": null,
      "genus": "Enterobacter",
      "familia": "Enterobacteriaceae",
      "classis": "Gammaproteobacteria",
      "phylum": "Proteobacteria",
      "regio": "Bacteria",
      "authors": "Zhu et al. 2011",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 61:2769*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterobacter.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-26271.html",
      "literature": [
        {
          "pubmed": "21216919",
          "reference": "Zhu, B., Lou, M. M., Xie, G. L., Wang, G. F., Zhou, Q., Wang, F., Fang, Y., Su, T., Li, B., Duan, Y. P. (2011). <i>Enterobacter mori</i> sp. nov., associated with bacterial wilt on <i>Morus alba</i> L. <i> Int J Syst Evol Microbiol </i><b> 61 </b> ( Pt 11 ): 2769-2774 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "R18-2",
        "CGMCC 1.10322",
        "LMG 25706",
        "DSM 26271",
        "R-18-2"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterobacter+mori"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/789938/",
      "pnu_no": 789938,
      "label": "Enterococcus quebecensis",
      "species": "Enterococcus quebecensis",
      "species_epithet": "quebecensis",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Sistek et al. 2012",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 62:1314*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-23327.html",
      "literature": [
        {
          "pubmed": "21788227",
          "reference": "Sistek, V., Maheux, A. F., Boissinot, M., Bernard, K. A., Cantin, P., Cleenwerck, I., De Vos, P., Bergeron, M. G. (2012). <i>Enterococcus ureasiticus</i> sp. nov. and <i>Enterococcus quebecensis</i> sp. nov., isolated from water. <i> Int J Syst Evol Microbiol </i><b> 62 </b> ( Pt 6 ): 1314-1320 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "CCRI-16985",
        "CCUG 59306",
        "DSM 23327",
        "LMG 26306"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+quebecensis"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/789939/",
      "pnu_no": 789939,
      "label": "Enterococcus ureasiticus",
      "species": "Enterococcus ureasiticus",
      "species_epithet": "ureasiticus",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Sistek et al. 2012",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 62:1314*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-23328.html",
      "literature": [
        {
          "pubmed": "21788227",
          "reference": "Sistek, V., Maheux, A. F., Boissinot, M., Bernard, K. A., Cantin, P., Cleenwerck, I., De Vos, P., Bergeron, M. G. (2012). <i>Enterococcus ureasiticus</i> sp. nov. and <i>Enterococcus quebecensis</i> sp. nov., isolated from water. <i> Int J Syst Evol Microbiol </i><b> 62 </b> ( Pt 6 ): 1314-1320 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "CCRI-16986",
        "CCUG 59304",
        "DSM 23328",
        "LMG 26304"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+ureasiticus"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/789983/",
      "pnu_no": 789983,
      "label": "Enterococcus plantarum",
      "species": "Enterococcus plantarum",
      "species_epithet": "plantarum",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "&#x0160;vec et al. 2012",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 62:1499*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-26408.html",
      "literature": [
        {
          "pubmed": "21856982",
          "reference": "Svec, P., Vandamme, P., Bryndová, H., Holochová, P., Kosina, M., Ma¨lanová, I., Sedlácek, I. (2012). <i>Enterococcus plantarum</i> sp. nov., isolated from plants. <i> Int J Syst Evol Microbiol </i><b> 62 </b> ( Pt 7 ): 1499-1505 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "C27",
        "CCM 7889",
        "LMG 26214",
        "DSM 26408"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+plantarum"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/789995/",
      "pnu_no": 789995,
      "label": "Leuconostoc mesenteroides subsp. suionicum",
      "species": "Leuconostoc mesenteroides subsp. suionicum",
      "species_epithet": "mesenteroides",
      "subspecies_epithet": "suionicum",
      "genus": "Leuconostoc",
      "familia": "Leuconostocaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Gu et al. 2012",
      "taxon": "subsp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 62:1548*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/leuconostoc.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-20241.html",
      "literature": [
        {
          "pubmed": "21856976",
          "reference": "Gu, C. T., Wang, F., Li, C. Y., Liu, F., Huo, G. C. (2012). <i>Leuconostoc mesenteroides</i> subsp. suionicum subsp. nov.. <i> Int J Syst Evol Microbiol </i><b> 62 </b> ( Pt 7 ): 1548-1551 ."
        }
      ],
      "correct_name": [
        "https://bacdive.dsmz.de/api/pnu/species/795521/",
        "Leuconostoc suionicum"
      ],
      "synonyms": null,
      "type_strain": [
        "ATCC 9135",
        "DSM 20241",
        "LMG 8159",
        "NCIMB 6992"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Leuconostoc+suionicum"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/790081/",
      "pnu_no": 790081,
      "label": "Enterococcus lactis",
      "species": "Enterococcus lactis",
      "species_epithet": "lactis",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Morandi et al. 2012",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 62:1992*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-23655.html",
      "literature": [
        {
          "pubmed": "22003038",
          "reference": "Morandi, S., Cremonesi, P., Povolo, M., Brasca, M. (2012). <i>Enterococcus lactis</i> sp. nov., from Italian raw milk cheeses. <i> Int J Syst Evol Microbiol </i><b> 62 </b> ( Pt 8 ): 1992-1996 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "BT159",
        "DSM 23655",
        "LMG 25958"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+lactis"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/790135/",
      "pnu_no": 790135,
      "label": "Enterococcus rivorum",
      "species": "Enterococcus rivorum",
      "species_epithet": "rivorum",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Niemi et al. 2012",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 62:2169*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": null,
      "literature": [
        {
          "pubmed": "22058322",
          "reference": "Niemi, R. M., Ollinkangas, T., Paulin, L., Svec, P., Vandamme, P., Karkman, A., Kosina, M., Lindström, K. (2012). <i>Enterococcus rivorum</i> sp. nov., from water of pristine brooks. <i> Int J Syst Evol Microbiol </i><b> 62 </b> ( Pt 9 ): 2169-2173 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "S299",
        "CCM 7986",
        "HAMBI 3055",
        "LMG 25899",
        "DSM 104544"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+rivorum"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/790533/",
      "pnu_no": 790533,
      "label": "Enterococcus rotai",
      "species": "Enterococcus rotai",
      "species_epithet": "rotai",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Sedláu0010Dek et al. 2013",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 63:502*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-102982.html",
      "literature": [
        {
          "pubmed": "22523160",
          "reference": "Sedlácek, I., Holochová, P., Maslanová, I., Kosina, M., Spröer, C., Bryndová, H., Vandamme, P., Rudolf, I., Hubálek, Z., Svec, P. (2013). <i>Enterococcus ureilyticus</i> sp. nov. and <i>Enterococcus rotai </i>sp. nov., two urease-producing enterococci from the environment. <i> Int J Syst Evol Microbiol </i><b> 63 </b> ( Pt 2 ): 502-10 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "CCM 4630",
        "CCUG 61593",
        "LMG 26678",
        "DSM 102982"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+rotai"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/790534/",
      "pnu_no": 790534,
      "label": "Enterococcus ureilyticus",
      "species": "Enterococcus ureilyticus",
      "species_epithet": "ureilyticus",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Sedláu0010Dek et al. 2013",
      "taxon": "sp. nov. (VP)",
      "reference": "Int. J. Syst. Evol. Microbiol. 63:502*",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-102981.html",
      "literature": [
        {
          "pubmed": "22523160",
          "reference": "Sedlácek, I., Holochová, P., Maslanová, I., Kosina, M., Spröer, C., Bryndová, H., Vandamme, P., Rudolf, I., Hubálek, Z., Svec, P. (2013). <i>Enterococcus ureilyticus</i> sp. nov. and <i>Enterococcus rotai </i>sp. nov., two urease-producing enterococci from the environment. <i> Int J Syst Evol Microbiol </i><b> 63 </b> ( Pt 2 ): 502-10 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "CCM 4629",
        "CCUG 48799",
        "LMG 26676",
        "DSM 102981"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+ureilyticus"
    },
    {
      "url": "https://bacdive.dsmz.de/api/pnu/species/790806/",
      "pnu_no": 790806,
      "label": "Enterococcus eurekensis",
      "species": "Enterococcus eurekensis",
      "species_epithet": "eurekensis",
      "subspecies_epithet": null,
      "genus": "Enterococcus",
      "familia": "Enterococcaceae",
      "classis": "Bacilli",
      "phylum": "Firmicutes",
      "regio": "Bacteria",
      "authors": "Cotta et al. 2013",
      "taxon": "sp. nov. (VL)",
      "reference": "Int. J. Syst. Evol. Microbiol. 63:2365",
      "comment": null,
      "lpsn": "http://www.bacterio.net/enterococcus.html",
      "wink_compendium": null,
      "dsmz_catalogue": "http://www.dsmz.de/catalogues/details/culture/DSM-105068.html",
      "literature": [
        {
          "pubmed": null,
          "reference": "(2013). List of new names and new combinations previously effectively, but not validly, published. <i> Int J Syst Evol Microbiol </i><b> 63 </b> ( Pt 7 ): 2365-2367 ."
        },
        {
          "pubmed": "23592176",
          "reference": "Cotta, M. A., Whitehead, T. R., Falsen, E., Moore, E., Lawson, P. A. (2013). Erratum to: Two novel species <i>Enterococcus lemanii</i> sp. nov. and <i>Enterococcus eurekensis</i> sp. nov., isolated from a swine-manure storage pit. <i> Antonie Van Leeuwenhoek </i><b> 103 </b> ( 6 ): 1409-18 ."
        }
      ],
      "correct_name": null,
      "synonyms": null,
      "type_strain": [
        "PC4B",
        "CCUG 61259",
        "NRRL B-59662",
        "DSM 105068"
      ],
      "bacdive": "http://bacdive.dsmz.de/index.php?search=Enterococcus+eurekensis"
    }
  ]
}
```
