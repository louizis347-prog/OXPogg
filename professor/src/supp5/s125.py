"""Suplemento Quest v5 · aula 125: At the doctor's office + regular Don't Be Nervous (The Lion and the Mouse)."""
SUPP = {
 'reg': 57,
 'badge': {'icon': '🩺', 'name': 'Patient Voice', 'desc': 'Tell a doctor what is wrong, in English'},
 'culture': {
  'hook': 'At a US doctor’s office, the doctor asks short questions: What is the problem? How long? Do you have a fever? Clear, simple answers help a lot.',
  'mythfact': [
   {'s': 'You say “I have a sore throat” when your throat hurts.', 'ans': True, 'why': 'Sore throat is the normal phrase.'},
   {'s': 'The doctor often asks, “How long do you have the problem?”', 'ans': True, 'why': 'They want to know when it started, for example “Since Monday.”'},
   {'s': 'You must say “doctor, doctor” before every sentence.', 'ans': False, 'why': 'A simple “Thank you, doctor” is enough.'},
   {'s': 'In many places, a nurse checks your weight and temperature first.', 'ans': True, 'why': 'This often happens before you see the doctor.'},
   {'s': '“The Lion and the Mouse” is a fable about a small mouse that helps a lion.', 'ans': True, 'why': 'The mouse frees the lion from a net.'}],
  'wild': [
   {'kind': 'Patient form', 'lines': ['**Reason for visit:** sore throat and cough', '**Since:** Monday', '**Fever?** ☐ Yes ☑ No'], 'decode': {'q': 'Does the patient have a fever?', 'opts': ['No', 'Yes', 'The form does not say'], 'ans': 0, 'why': 'The box No is marked.'}},
   {'kind': 'Sign in the waiting room', 'lines': ['Please **sign in** at the desk.', 'Wear a mask if you **cough**.', 'The doctor will call your name.'], 'decode': {'q': 'What does the doctor do?', 'opts': ['Calls your name', 'Calls your phone', 'Comes to the desk'], 'ans': 0, 'why': 'The sign says the doctor will call your name.'}}],
  'compare': {'br': 'In Brazil, many people say “Doutor, estou com dor de garganta há três dias” and the doctor may also ask about allergies.', 'us': 'In the USA, the staff ask your name, birthday and insurance first. Then the doctor asks short questions about your problem.', 'tip': 'Answer with the problem and the time: “I have a cough. Since Monday.”', 'ask': 'How do you say that your throat hurts? Say it in English.'},
  'quiz': [
   {'q': 'The doctor asks, “What’s the problem?” You say…', 'opts': ['I have a sore throat and a cough.', 'I am sore throat.', 'I problem throat.'], 'ans': 0, 'why': 'I have + the problem is the natural answer.'},
   {'q': 'The doctor asks, “How long?” You have it for three days. You say…', 'opts': ['Since Monday. Three days.', 'On Monday three.', 'I have three.'], 'ans': 0, 'why': 'Since + start day, then say the number of days.'},
   {'q': 'The doctor says, “Open your mouth, please.” You…', 'opts': ['Open your mouth and say “ah.”', 'Say “thank you” and sit.', 'Close your eyes.'], 'ans': 0, 'why': 'The doctor looks at your throat.'}]},
 'reading': {
  'genre': 'Story',
  'title': 'A visit to the doctor in Seattle',
  'text': [
   'Reed is in **Seattle**. It is a cold, wet week, and he does not feel good. His **throat** hurts, and he has a **cough**. He goes to the doctor’s office on Thursday.',
   'In the waiting room, he is a little nervous, like the small mouse in the fable. “**Don’t be nervous**,” he says to himself. A nurse calls his name, and he follows her to a small room.',
   'Dr. Mei comes in and says, “Hello. **Please sit down.**” Reed says, “**Thank you, doctor.**” She smiles and asks, “**What’s the problem?**” He answers, “**I have a sore throat and a cough.**”',
   'The doctor asks, “**How long do you have them?**” Reed says, “**Since Monday. Three days.**” She asks, “**Do you have a fever?**” “**No, I don’t**,” he says. She looks at the paper from the nurse. His temperature is normal.',
   'Then the doctor says, “**Open your mouth**, please. Say ‘ah’.” Reed opens his **mouth** and says, “Ahhh.” She uses a small light and looks inside. Reed feels fine and not afraid at all.',
   'The doctor says, “It is a small problem. Drink warm water and rest. Come back if it is not better.” Reed says, “Thank you.” He feels calm. The doctor, like the lion in the fable, is kind.'],
  'glossary': [{'w': 'throat', 'pt': 'garganta'}, {'w': 'cough', 'pt': 'tosse'}, {'w': 'waiting room', 'pt': 'sala de espera'}, {'w': 'nervous', 'pt': 'nervoso'}, {'w': 'nurse', 'pt': 'enfermeira'}, {'w': 'sore', 'pt': 'dolorido'}, {'w': 'temperature', 'pt': 'temperatura'}, {'w': 'mouth', 'pt': 'boca'}, {'w': 'light', 'pt': 'lanterna, luz'}, {'w': 'calm', 'pt': 'calmo'}],
  'fast': {'q': 'What is this text about?', 'opts': ['A patient with a sore throat', 'A cooking contest', 'A day at the beach'], 'ans': 0, 'why': 'Reed visits Dr. Mei with a sore throat and a cough.'},
  'scan': [{'q': 'What is the doctor’s name?', 'ans': 'Dr. Mei', 'alt': ['mei']}, {'q': 'Since what day does Reed have the problem?', 'ans': 'Monday', 'alt': ['since monday', 'monday']}, {'q': 'What does the doctor look at with a light?', 'ans': 'mouth', 'alt': ['his mouth', 'throat', 'inside his mouth']}],
  'tf': [
   {'s': 'Reed has a fever.', 'ans': False, 'why': 'He says, “No, I don’t.”'},
   {'s': 'Reed has the problem for three days.', 'ans': True, 'why': 'He says, “Since Monday. Three days.”'},
   {'s': 'The doctor asks Reed to open his mouth.', 'ans': True, 'why': 'She says, “Open your mouth, please.”'},
   {'s': 'The doctor says the problem is very big.', 'ans': False, 'why': 'She says it is a small problem.'}],
  'order': ['Reed goes to the doctor’s office.', 'A nurse calls his name.', 'The doctor asks, “What’s the problem?”', 'Reed opens his mouth.', 'The doctor says to drink warm water and rest.'],
  'ctx': [
   {'sent': 'He is a little nervous.', 'w': 'nervous', 'opts': ['a bit worried', 'very strong', 'very hungry'], 'ans': 0, 'why': 'Nervous = worried before something.'},
   {'sent': 'His temperature is normal.', 'w': 'temperature', 'opts': ['how hot the body is', 'how tall the body is', 'how old the person is'], 'ans': 0, 'why': 'Temperature = how hot or cold something is.'},
   {'sent': 'He feels calm.', 'w': 'calm', 'opts': ['quiet and relaxed', 'angry', 'very tired'], 'ans': 0, 'why': 'Calm = relaxed, not worried.'}],
  'chunkHunt': ['What’s the problem?', 'I have a sore throat and a cough.', 'Since Monday.', 'Open your mouth, please.'],
  'think': 'Are you nervous at the doctor’s office? What can you say to feel better?'},
 'convo': {'npc': {'name': 'Dr. Mei'}, 'story': 'You are at the doctor’s office in Seattle. Dr. Mei asks about your problem.', 'turns': [
  {'npc': 'Hello. Please sit down.', 'pt': 'Olá. Sente-se, por favor.', 'opts': [
   {'en': 'Thank you, doctor.', 'pt': 'Obrigado, doutora.', 'ok': True, 'fb': 'Polite and short.'},
   {'en': 'You sit down.', 'pt': 'Você senta.', 'ok': False, 'fb': 'It sounds like an order.'},
   {'en': 'I am a doctor.', 'pt': 'Sou médico.', 'ok': False, 'fb': 'You are the patient.'}]},
  {'npc': 'What’s the problem?', 'pt': 'Qual é o problema?', 'opts': [
   {'en': 'I am sore throat.', 'pt': 'Eu sou dor de garganta.', 'ok': False, 'fb': 'Use have: I have a sore throat.'},
   {'en': 'I have a sore throat and a cough.', 'pt': 'Estou com dor de garganta e tosse.', 'ok': True, 'fb': 'Use have + the problem.'},
   {'en': 'The problem is Monday.', 'pt': 'O problema é segunda.', 'ok': False, 'fb': 'It does not say what hurts.'}]},
  {'npc': 'How long do you have them?', 'pt': 'Há quanto tempo?', 'opts': [
   {'en': 'Since Monday. Three days.', 'pt': 'Desde segunda. Três dias.', 'ok': True, 'fb': 'Give the start day and the time.'},
   {'en': 'For Monday.', 'pt': 'Por segunda.', 'ok': False, 'fb': 'Use since with a start day.'},
   {'en': 'I have long.', 'pt': 'Eu tenho longo.', 'ok': False, 'fb': 'Not a natural answer.'}]},
  {'npc': 'Do you have a fever?', 'pt': 'Você tem febre?', 'opts': [
   {'en': 'No, I’m not.', 'pt': 'Não, eu não sou.', 'ok': False, 'fb': 'The question uses do: No, I don’t.'},
   {'en': 'Yes, a sore throat.', 'pt': 'Sim, dor de garganta.', 'ok': False, 'fb': 'It does not answer about fever.'},
   {'en': 'No, I don’t.', 'pt': 'Não, não tenho.', 'ok': True, 'fb': 'Short answer with don’t.'}]},
  {'npc': 'Open your mouth, please. Say “ah.”', 'pt': 'Abra a boca, por favor. Diga “ah”.', 'opts': [
   {'en': 'Ahhh.', 'pt': 'Aaah.', 'ok': True, 'fb': 'Just do it and say ah.'},
   {'en': 'Open your mouth, doctor.', 'pt': 'Abra a boca, doutora.', 'ok': False, 'fb': 'It is the doctor’s request.'},
   {'en': 'I have a mouth.', 'pt': 'Eu tenho uma boca.', 'ok': False, 'fb': 'It is not a useful answer.'}]}]},
 'homework': 'Say 4 sentences to a doctor: what hurts, since when, if you have a fever and a polite thanks. Record and send them.',
 'homework_items': ['Say: I have a sore throat and a cough.', 'Write 3 sentences with since + a day.', 'Listen to the dialogue and repeat each line.', 'Review: What’s the problem? / How long? / Do you have a fever?'],
 'errors': [
  {'wrong': 'I am cough.', 'fix': 'I have a cough.', 'alt': 'I have cough a.', 'why': 'For symptoms, use have a + noun.'},
  {'wrong': 'My throat is hurt.', 'fix': 'My throat hurts.', 'alt': 'My throat hurting.', 'why': 'Hurt is a verb here: my throat hurts.'},
  {'wrong': 'No, I haven’t.', 'fix': 'No, I don’t.', 'alt': 'No, I don’t have not.', 'why': 'Answer Do you have…? with No, I don’t.'},
  {'wrong': 'Open the mouth, please.', 'fix': 'Open your mouth, please.', 'alt': 'Open you mouth, please.', 'why': 'Use your with body parts.'}],
}
