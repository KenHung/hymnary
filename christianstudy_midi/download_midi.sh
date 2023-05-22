for i in $(seq -f "%03g" 1 716)
do
  curl http://www.christianstudy.com/data/hymns/midi/hymnary/hymnary$i.mid --output hymnary$i.mid
done
