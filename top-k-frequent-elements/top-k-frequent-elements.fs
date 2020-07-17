let topKFrequent nums k =
    nums |> Seq.countBy id |> Seq.sortByDescending snd |> Seq.take k |> Seq.map fst |> Seq.toList