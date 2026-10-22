// Create a Text parameter DataFolder for the evidence folder path.
let
    Source = Csv.Document(File.Contents(DataFolder & "/fact_requests.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Headers = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    EmptyDates = Table.ReplaceValue(Headers, "", null, Replacer.ReplaceValue, {"submitted_date"}),
    Typed = Table.TransformColumnTypes(EmptyDates, {{"source_id", type text}, {"submitted_date", type date}, {"branch_code", type text}, {"outcome", type text}}, "en-US")
in
    Typed
