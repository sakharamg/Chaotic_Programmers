import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.stream.Collectors;

public class Q1 {

	public static void main(String[] args) {

		String file1path = args[0];
		String file2path = args[1];

		Map<String, Integer> map = new LinkedHashMap<>();

		File f1 = new File(file1path);
		File f2 = new File(file2path);
		try {
			BufferedReader f1buffer = new BufferedReader(new FileReader(f1));
			String line;
			while ((line = f1buffer.readLine()) != null) {
				if (!map.containsKey(line.strip())) {
					map.put(line.strip(), 1);
				} else {
					map.put(line.strip(), map.get(line.strip()) + 1);
				}
			}
			f1buffer.close();
			BufferedReader f2buffer = new BufferedReader(new FileReader(f2));
			while ((line = f2buffer.readLine()) != null) {
				if (map.containsKey(line.strip())) {
					map.remove(line.strip());
				}
			}
			f2buffer.close();
			java.util.List<Map.Entry<String, Integer>> l = map.entrySet().stream().collect(Collectors.toList());
			Collections.sort(l, new Comparator<Map.Entry<String, Integer>>() {
				@Override
				public int compare(Entry<String, Integer> o1, Entry<String, Integer> o2) {
					if (o1.getValue().compareTo(o2.getValue()) == 0) {
						return o1.getKey().compareTo(o2.getKey());
					} else
						return -1*o1.getValue().compareTo(o2.getValue());

				}
			});
			//Collections.reverse(l);

			for (int i = 0; i < l.size(); i++) {
				System.out.println(l.get(i).getKey() + "," + l.get(i).getValue());
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
