# `gan-aidraft` Command Reference

The `gan-aidraft` command is a tool for generating candidate GAN roots from a text passage using a large language model (LLM) hosted on OpenRouter.

## Synopsis

```bash
usage: gan-aidraft [-h] -i INPUT -o OUTPUT [--api API_KEY] [-m MODEL] [--quality-model QUALITY_MODEL] [--quiet] [--timeout TIMEOUT] [--max-retries MAX_RETRIES]
```

## Description

This script takes a text file as input, sends its content to an OpenRouter-hosted LLM, and asks it to generate a table of relevant linguistic roots (lexemes). The LLM's output is then passed through a quality filter (which may use a different LLM) to validate and normalize the entries. The final, high-quality rows are saved to a TSV file. This is useful for quickly bootstrapping a lexicon of roots from a descriptive text about a specific topic.

## Options

*   `-h, --help`: Shows the help message and exits.
*   `-i, --input <file>`: **Required**. Path to the input text file. Use `-` to read from stdin.
*   `-o, --output <file>`: **Required**. The path for the output TSV file.
*   `--api <key>`: *Optional*. Your OpenRouter API key. Can also be set via the `OPENROUTER_API_KEY` environment variable.
*   `-m, --model <identifier>`: *Optional*. The identifier for the LLM to use for generation (e.g., `openai/gpt-4o-mini`). Defaults to the value of the `OPENROUTER_MODEL` environment variable, or `openai/gpt-4o-mini` if not set.
*   `--quality-model <identifier>`: *Optional*. The identifier for the LLM to use for quality filtering. Defaults to the generation model. Can also be set via `OPENROUTER_QUALITY_MODEL`.
*   `--quiet`: *Optional*. Suppress progress information written to stderr.
*   `--timeout <seconds>`: *Optional*. HTTP timeout for OpenRouter API calls in seconds. Defaults to 60.
*   `--max-retries <count>`: *Optional*. Maximum number of retries for failed API requests. Defaults to 4.

## Environment Variables

*   `OPENROUTER_API_KEY`: Can be used to provide the API key instead of the `--api` flag.
*   `OPENROUTER_MODEL`: Can be used to specify the default generation model.
*   `OPENROUTER_QUALITY_MODEL`: Can be used to specify the default quality-filtering model.

## Example

To generate roots from a file named `my_topic.txt` and save them to `roots.tsv`, using a specific model:

```bash
export OPENROUTER_API_KEY="your_secret_key_here"
gan-aidraft -i my_topic.txt -o roots.tsv -m "anthropic/claude-3.5-sonnet"
```

This will create `roots.tsv` containing the generated and filtered lexicon entries.

### Example input

In `tests/abstract.txt`:

```text
```

### Execution

During execution the program produces a verbose log, explaining which rows were kept or dropped by the quality filter:

```text
gan-ai -i tests/abstract.txt  -o test-ai 
Reading context from tests/abstract.txt...
Requesting candidate rows from model 'openai/gpt-oss-120b:exacto'...
Received 16 raw row(s) from model response.
Normalized to 16 unique row(s) after coercion and de-duplication.
[KEEP] Row 1: Equus — Root not proper Latin genitive stem; should be 'equi' for Equus
[KEEP] Row 2: Intestinum — Root not proper genitive stem; corrected to intestini.
[KEEP] Row 3: (unnamed) — Entry meets all nomenclatural criteria
[KEEP] Row 4: ἔντερον — Minor gender formatting; add trailing space.
[KEEP] Row 5: microbioma — Entry conforms to Neo‑Latin format, proper gender, part of speech, ASCII root, and includes article and explanation.
[KEEP] Row 6: bacterium — Minor formatting: gender lacks required trailing space.
[KEEP] Row 7: (unnamed) — Entry well‑formed; all fields conform to Neo‑Latin standards.
[KEEP] Row 8: φάγος — All fields conform to guidelines: Greek language, proper Greek script, ASCII Latinized root, correct gender/part, valid definition and explanation.
[DROP] Row 9: Feces — Word 'Feces' is modern English spelling, not proper Latin; root 'fec' is not correctly Latinized.
[KEEP] Row 10: Fibra — Root must be genitive stem for Latin noun; corrected to fibrae.
[DROP] Row 11: metagenomica — Word is modern English masquerading as Latin; root 'metagen' is not Latinized; definition lacks an article.
[KEEP] Row 12: Candidatus — Root not proper genitive; should be 'candidati'
[...]
```

### Example output

:warning: Being generated using LLMs, **the output must be carefully reviewed and validated** before use.
Also, the process is stochastic, so different runs may produce different results.

This is an example output produced by the model `openai/gpt-oss-120b:exacto` on the input file `tests/abstract.txt`:

|Language|Gender|Part|Word|Root|Definition|Explanation|
|---|---|---|---|---|---|---
|L.|masc.|n.|equus|equ-|horse|horses|
|Gr.|masc.|n.|hippus|hipp-|horse (Greek)|horses|
|L.|neut.|n.|intestinum|intestin-|intestine, gut|gut|
|L.|neut.|n.|bacterium|bacteri-|bacterium|bacteria|
|L.|masc.|n.|candidatus|candid-|provisional taxonomic status for uncultured organisms|taxonomy|
|L.|neut.|n.|genus|gen-|taxonomic rank above species|taxonomy|
|L.|fem.|n.|species|speci-|basic unit of classification|taxonomy|
|L.|f.|n.|sequentia|sequ-|process of determining nucleotide order|sequencing|

and this is another output:

|Language|Gender|Part|Word|Root|Definition|Explanation|
|---|---|---|---|---|---|---
|L.|masc.|n.|Equus|equi|a horse|Host-Animal-Mammal-Equine|
|L.|neut.|n.|Intestinum|intestini|the intestine|Host-Animal-System-Digestive-Intestine|
|Gr.|neut.|n.|ἔντερον|enter|the gut|Host-Animal-System-Digestive-Enteric|
|N.L.|neut.|n.|microbioma|microbio|the microbiome|Microbial-Community-Host-Associated|
|N.L.|neut.|n.|bacterium|bacteri|a bacterium|Microbe-Bacteria|
|Gr.|masc.|n.|φάγος|phago|a bacteriophage|Virus-Phage|
|L.|fem.|n.|Fibra|fibrae|a fibre|Dietary-Fibre|
|L.|masc.|n.|Candidatus|candidati|a provisional taxon|Taxonomic-Status|
|L.|neut.|n.|Genus|gener|a genus|Taxonomic-Rank|
|L.|fem.|n.|Species|speciei|a species|Taxonomic-Rank|
|L.|neut.|n.|Caecum|caeci|the hindgut cecum|Host-Animal-System-Digestive-Hindgut|
