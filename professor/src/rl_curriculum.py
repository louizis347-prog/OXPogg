#!/usr/bin/env python3
"""Currículo do Painel do Professor — Real-Life English: 100 aulas em 13 unidades (A1: 70, A2: 30).
Cada aula: situação real + padrões principais + insight cultural + cenário e personagens (nomes de data/elenco.json).
Uso: python3 src/rl_curriculum.py  →  data/v3/curriculum.json"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
U = []  # (unit_n, level, name, [lessons])


def L(title, pt, scene, cast, patterns, culture):
    return dict(title=title, pt=pt, scene=scene, cast=cast.split('+'), patterns=patterns, culture=culture)


U.append((1, 'A1', 'Real-Life English: first week', [
    L('Meeting new people', 'Conhecer pessoas', 'park', 'Mia+Ken', "I'm… / Are you…? / Where are you from? / Nice to meet you", 'First names, handshakes vs smiles, small talk about the weather'),
    L('Talking about routines', 'Falar da rotina', 'livingroom', 'Ana+Tom', 'I usually… / Do you…? / What time do you…?', 'Typical US/UK daily schedules: breakfast, commute, lunch'),
    L('Ordering at a café', 'Pedir num café', 'cafe', 'Luis+Mia', 'Can I get…? / I’d like… / Do you have…? / For here or to go?', 'Coffee shop culture, sizes, customization, tipping'),
    L('Shopping for clothes', 'Comprar roupas', 'market', 'Ali+Lily', 'How much is…? / Do you have this in…? / Can I try it on?', 'Sizes (US vs UK vs Brazil), fitting rooms, return policies'),
    L('Asking for directions', 'Pedir direções', 'city', 'Cleo+Raj', 'Where is…? / How do I get to…? / Turn left / It’s next to…', 'Blocks vs streets, giving directions politely, using maps apps'),
    L('Making plans', 'Combinar programas', 'park', 'Maya+Ben', "Let’s… / How about…? / Are you free on…? / Sounds good!", 'Texting plans, “let’s grab a coffee”, being on time'),
    L('Solving everyday problems', 'Resolver problemas do dia a dia', 'office', 'Hugo+Zoe', 'I need… / Could you…? / It doesn’t work / Can you help me?', 'Asking for help politely and how people apologize'),
    L('Real-Life Mission Day 1', 'Missão da unidade 1', 'plaza', 'Mia+Ken+Luis', 'meet · order · ask · plan · solve', 'Integrated mission: a first day in a new neighborhood')]))
U.append((2, 'A1', 'Home & family', [
    L('Introducing family and friends', 'Apresentar família e amigos', 'livingroom', 'Rosa+Diego', 'This is my… / He’s / She’s… / How old is…?', 'Family photos, introducing people politely'),
    L('Describing your home', 'Descrever a casa', 'bedroom', 'Ida+Sam', 'There is / There are… / It’s next to… / I have a…', 'Apartments vs houses, rooms and rent'),
    L('Chores and house rules', 'Tarefas e regras da casa', 'kitchen', 'Lucia+Ivan', 'Can you…? / Please don’t… / It’s my turn to…', 'Sharing chores, roommates, polite reminders'),
    L('Talking about jobs', 'Falar de profissões', 'office', 'Raj+Amy', 'What do you do? / I work as… / Where do you work?', 'Small talk about work, titles'),
    L('Birthdays and invitations', 'Aniversários e convites', 'livingroom', 'Lena+Gus', 'Would you like to come…? / I’d love to / Sorry, I can’t', 'Party customs, gifts, RSVP'),
    L('Phone calls and voice messages', 'Ligações e mensagens de voz', 'bedroom', 'Dani+Beto', 'Can I speak to…? / It’s … speaking / Can you call back?', 'Phone etiquette, voicemail, texting vs calling'),
    L('Visiting a neighbor', 'Visitar um vizinho', 'corridor', 'Pru+Kofi', 'Could you…? / Do you mind if…? / Thanks for having me', 'Neighbor culture, borrowing things, apartment buildings'),
    L('Real-Life Mission Day 2', 'Missão da unidade 2', 'livingroom', 'Rosa+Diego+Pru', 'introduce · describe · invite · ask a favor', 'Integrated mission: hosting a small dinner')]))
U.append((3, 'A1', 'Eating out & shopping', [
    L('Ordering in a restaurant', 'Pedir num restaurante', 'restaurant', 'Andre+Sofia', 'I’ll have… / Could we have…? / What do you recommend?', 'Tipping in the US, waiter names, “check, please”'),
    L('Fast food and takeout', 'Fast food e pedidos para viagem', 'diner', 'Bella+Jin', 'Can I get a… with…? / Without… / For here or to go?', 'Combos, drive-through, sizes'),
    L('At the supermarket', 'No supermercado', 'supermarket', 'Dina+Hana', 'Where can I find…? / Is there any…? / How much is…?', 'Aisles, self-checkout, bringing your own bag'),
    L('At the market: quantities', 'Na feira: quantidades', 'market', 'Rosa+Pablo', 'How much / How many…? / A kilo of… / A bag of…', 'Farmers markets, pounds vs kilos'),
    L('Asking for the bill and paying', 'Pedir a conta e pagar', 'restaurant', 'Leo+Tessa', 'Could we have the check, please? / Card or cash? / Keep the change', 'Tipping percentages, splitting the bill'),
    L('Food likes and dislikes', 'Gostos e desgostos de comida', 'kitchen', 'Remy+Nina', 'I like… / I don’t like… / I’m allergic to… / I prefer…', 'Allergies, dietary choices, polite refusals'),
    L('Following a simple recipe', 'Seguir uma receita simples', 'kitchen', 'Dev+Suri', 'First… / Then… / Add… / Mix…', 'Imperative in recipes, measurements'),
    L('Real-Life Mission Day 3', 'Missão da unidade 3', 'restaurant', 'Andre+Sofia+Bella', 'order · ask · pay · recommend', 'Integrated mission: dinner out with friends')]))
U.append((4, 'A1', 'Getting around', [
    L('Taking the bus or subway', 'Pegar ônibus ou metrô', 'subway', 'Tom+Elif', 'Which line…? / How many stops…? / Does this go to…?', 'Metro cards, rush hour, giving up your seat'),
    L('At the train station', 'Na estação de trem', 'station', 'Marco+Nora', 'One ticket to… / What time is the next…? / Which platform?', 'Round-trip, peak times, announcements'),
    L('Checking in at the airport', 'Fazer check-in no aeroporto', 'airport', 'Eva+Noah', 'I’d like to check in / Window or aisle? / Where is gate…?', 'Security, boarding passes, luggage rules'),
    L('Taking a taxi or rideshare', 'Pegar táxi ou aplicativo', 'road', 'Tariq+Isla', 'Could you take me to…? / How long will it take? / Stop here, please', 'Rideshare apps, tipping drivers'),
    L('Renting a bike or a car', 'Alugar bicicleta ou carro', 'road', 'Greta+Otto', 'How much per day? / Do I need…? / Is it insured?', 'Driver’s license, deposits, helmets'),
    L('When you are lost', 'Quando você se perde', 'city', 'Cleo+Theo', 'Excuse me, I’m lost / Could you show me on the map? / Is it far?', 'Asking strangers for help, landmarks'),
    L('Hotel check-in', 'Check-in no hotel', 'hotel', 'Hugo+Kate', 'I have a reservation / What time is check-out? / Is breakfast included?', 'Front desk, room keys, late check-out'),
    L('Real-Life Mission Day 4', 'Missão da unidade 4', 'airport', 'Eva+Noah+Hugo', 'travel · ask · check in · find your way', 'Integrated mission: a weekend trip')]))
U.append((5, 'A1', 'Health & body', [
    L('At the pharmacy', 'Na farmácia', 'pharmacy', 'Dina+Sami', 'Do you have something for…? / How often should I take…? / Is it safe?', 'Over-the-counter vs prescription'),
    L('At the doctor', 'No médico', 'hospital', 'Nina+Max', 'What’s the matter? / I have a… / How long have you…?', 'Appointments, insurance, waiting rooms'),
    L('Describing symptoms', 'Descrever sintomas', 'hospital', 'Mei+Olga', 'My… hurts / I feel… / I have a headache', 'Body vocabulary, pain scale'),
    L('At the gym', 'Na academia', 'gym', 'Joe+Zara', 'How often do you…? / Can you show me…? / I’m trying to…', 'Gym etiquette, trainers'),
    L('Healthy habits', 'Hábitos saudáveis', 'park', 'Ruth+Abel', 'I try to… / I never… / How often…? / Do you…?', 'Running culture, healthy snacks'),
    L('Asking for help in an emergency', 'Pedir ajuda numa emergência', 'road', 'Pete+Tina', 'Help! / Call… / I need an ambulance / It’s an emergency', 'Emergency numbers (911/999), staying calm'),
    L('Making an appointment', 'Marcar uma consulta', 'office', 'Aya+Hugo', 'I’d like to make an appointment / Are you free on…? / Can I reschedule?', 'Booking by phone or app'),
    L('Real-Life Mission Day 5', 'Missão da unidade 5', 'hospital', 'Nina+Max+Dina', 'describe · ask · book · get help', 'Integrated mission: a sick day')]))
U.append((6, 'A1', 'School & work', [
    L('First day in class', 'Primeiro dia de aula', 'classroom', 'Mina+Ryo', 'I’m new here / Can you repeat that? / How do you spell…?', 'Classroom routines, using first names'),
    L('Asking about the schedule', 'Perguntar sobre horários', 'classroom', 'Alma+Zara', 'What time does… start? / When is…? / Is it on Monday?', '12-hour vs 24-hour time, class timetables'),
    L('At the library', 'Na biblioteca', 'library', 'Emma+Maya', 'Can I borrow…? / How long can I keep it? / Where can I find…?', 'Library cards, quiet rules'),
    L('Workplace small talk', 'Conversa informal no trabalho', 'office', 'Raj+Pia', 'How was your weekend? / Did you…? / Are you busy?', 'Coffee-break chat, safe topics'),
    L('A simple job interview', 'Entrevista de emprego simples', 'office', 'Tessa+Ian', 'Tell me about yourself / I’m good at… / I have experience in…', 'Interview etiquette, eye contact'),
    L('Emails and phone at work', 'E-mails e telefone no trabalho', 'office', 'Amy+Max', 'I’m writing to… / Could you send…? / Thanks for your help', 'Email openings and closings'),
    L('Meeting a colleague', 'Conhecer um colega', 'office', 'Hugo+Kira', 'Nice to meet you / I work in… / What’s your role?', 'Names, titles, business cards'),
    L('Real-Life Mission Day 6', 'Missão da unidade 6', 'office', 'Raj+Pia+Tessa', 'introduce · schedule · borrow · write', 'Integrated mission: your first week at a new job')]))
U.append((7, 'A1', 'Free time', [
    L('Hobbies and interests', 'Hobbies e interesses', 'park', 'Paul+Isla', 'I like to… / What do you do in your free time? / I’m into…', 'Popular hobbies, clubs'),
    L('Weekend plans and sports', 'Planos de fim de semana e esportes', 'stadium', 'Beto+Jonas', 'Do you want to…? / Let’s play… / Who’s your team?', 'Sports culture, tailgating'),
    L('At the cinema', 'No cinema', 'cinema', 'Will+Lola', 'Two tickets for… / What time is the show? / Did you like it?', 'Popcorn, previews, opinions'),
    L('Music and concerts', 'Música e shows', 'concert', 'Hana+Carlos', 'I love… / Have you ever been to…? / Who’s playing?', 'Live music, festival etiquette'),
    L('Going to a party', 'Ir a uma festa', 'livingroom', 'Jade+Finn', 'Can I bring…? / Nice to meet you / I’d better go', 'Arriving on time, bringing a dish'),
    L('Messages and social media', 'Mensagens e redes sociais', 'bedroom', 'Zara+Elif', 'Did you see…? / Send me the… / LOL, BTW', 'Texting abbreviations'),
    L('Making friends online', 'Fazer amigos online', 'bedroom', 'Jin+Kai', 'Where are you from? / What games do you play? / Add me', 'Online etiquette and safety'),
    L('Real-Life Mission Day 7', 'Missão da unidade 7', 'park', 'Paul+Isla+Beto', 'invite · plan · share · react', 'Integrated mission: a free Saturday')]))
U.append((8, 'A1', 'City life', [
    L('At the bank', 'No banco', 'bank', 'Fatima+Hugo', 'I’d like to open an account / How do I…? / Can I withdraw…?', 'ATMs, fees, saving'),
    L('At the post office', 'No correio', 'postoffice', 'Sam+Rosa', 'I’d like to send… / How much is postage? / How long will it take?', 'Stamps, tracking numbers'),
    L('Getting a haircut', 'Cortar o cabelo', 'studio', 'Sami+Kofi', 'Just a trim, please / Not too short / How much is…?', 'Barber culture, tipping'),
    L('A day at the park', 'Um dia no parque', 'park', 'Greta+Ben', 'It’s a nice day / Let’s have a picnic / Watch out!', 'Park rules, picnics'),
    L('Weather and seasons', 'Clima e estações', 'rainystreet', 'Nora+Kate', 'It’s sunny/rainy… / What’s the weather like? / I need an umbrella', 'Weather as small talk'),
    L('Taking photos and sightseeing', 'Tirar fotos e passear', 'liberty', 'Diego+Cleo', 'Could you take a picture of us? / How much is the ticket? / It’s beautiful!', 'Landmarks, tourist etiquette'),
    L('Prices and discounts', 'Preços e descontos', 'market', 'Ali+Lily', 'Is there a discount? / Can I pay by card? / It’s too expensive', 'Sales, coupons, bargaining'),
    L('Real-Life Mission Day 8', 'Missão da unidade 8', 'city', 'Fatima+Sam+Diego', 'ask · pay · decide · enjoy', 'Integrated mission: a city errands day')]))
U.append((9, 'A1', 'Travel & stories', [
    L('Telling about your weekend', 'Contar sobre o fim de semana', 'park', 'Mia+Ana', 'I went to… / We watched… / It was great', 'Weekend talk on Monday'),
    L('Telling a short story', 'Contar uma pequena história', 'livingroom', 'Colin+Vera', 'First… / Then… / After that… / Finally…', 'Storytelling openers'),
    L('Booking a trip', 'Reservar uma viagem', 'office', 'Eva+Hugo', 'I’d like to book… / How much is…? / Is it direct?', 'Online booking, deposits'),
    L('Tourist information', 'Informações turísticas', 'plaza', 'Cleo+Oscar', 'What can we see…? / How do we get to…? / Is it open today?', 'Tourist offices, passes'),
    L('Postcards and travel messages', 'Cartões e mensagens de viagem', 'beach', 'Kai+Una', 'Wish you were here / Having a great time / See you soon', 'Postcard conventions'),
    L('A1 Final Mission', 'Missão final do A1', 'airport', 'Mia+Ken+Eva', 'meet · order · ask · plan · travel', 'Integrated mission: an A1 trip from start to finish')]))
U.append((10, 'A2', 'Daily life: past and plans', [
    L('Last weekend (past simple)', 'O fim de semana passado', 'park', 'Ana+Tom', 'I visited… / Did you…? / We didn’t… / It was…', 'Telling a past event naturally'),
    L('Describing people', 'Descrever pessoas', 'cafe', 'Lola+Will', 'He’s tall / She has… / He looks… / She’s friendly', 'Polite descriptions'),
    L('Comparing things', 'Comparar coisas', 'market', 'Ali+Mara', 'It’s bigger than… / The cheapest… / Which is better?', 'Shopping comparisons'),
    L('Making and changing reservations', 'Fazer e mudar reservas', 'restaurant', 'Sofia+Max', 'I’d like to book a table / Can we change…? / For how many?', 'Booking etiquette'),
    L('Opinions and preferences', 'Opiniões e preferências', 'livingroom', 'Nadia+Raj', 'I think… / In my opinion… / I’d rather… / I agree', 'Polite disagreement'),
    L('Giving advice', 'Dar conselhos', 'cafe', 'Mina+Joe', 'You should… / Why don’t you…? / If I were you…', 'Advice among friends'),
    L('Talking about plans (going to)', 'Falar de planos', 'bedroom', 'Maya+Ben', 'I’m going to… / We’re planning to… / What are you going to do?', 'Future plans'),
    L('Real-Life Mission Day 10', 'Missão da unidade 10', 'plaza', 'Ana+Tom+Lola', 'tell · describe · compare · advise', 'Integrated mission: planning a group weekend')]))
U.append((11, 'A2', 'Services and problems', [
    L('Returning an item', 'Devolver um produto', 'market', 'Ali+Lily', 'I’d like to return… / It doesn’t fit / Can I get a refund?', 'Receipts, store credit'),
    L('Complaining politely', 'Reclamar com educação', 'restaurant', 'Leo+Tessa', 'I’m afraid there’s a problem / This isn’t what I ordered / Could you…?', 'Polite complaints'),
    L('Tech problems', 'Problemas de tecnologia', 'office', 'Kofi+Jin', 'It won’t turn on / I can’t log in / Have you tried…?', 'IT help desks'),
    L('Renting an apartment', 'Alugar um apartamento', 'livingroom', 'Ida+Ivan', 'How much is the rent? / Is it furnished? / When can I move in?', 'Deposits, leases'),
    L('Neighborhood issues', 'Problemas na vizinhança', 'corridor', 'Pru+Gus', 'It’s too noisy / Could you keep it down? / I’d appreciate…', 'Talking to neighbors'),
    L('Customer service calls', 'Ligações de atendimento', 'office', 'Amy+Raj', 'I’m calling about… / Could you hold on? / Let me check', 'Phone scripts'),
    L('Lost and found', 'Achados e perdidos', 'station', 'Hugo+Eva', 'I’ve lost my… / What does it look like? / Where did you last see it?', 'Describing lost items'),
    L('Real-Life Mission Day 11', 'Missão da unidade 11', 'office', 'Kofi+Ida+Amy', 'explain · complain · solve · follow up', 'Integrated mission: fixing a bad week')]))
U.append((12, 'A2', 'Culture and communication', [
    L('Invitations: accept and decline', 'Convites: aceitar e recusar', 'livingroom', 'Rosa+Diego', 'Would you like to…? / I’d love to, but… / Maybe next time', 'Declining politely'),
    L('Experiences (present perfect)', 'Experiências de vida', 'cafe', 'Raj+Nina', 'Have you ever…? / I’ve never… / I’ve been to…', 'Travel stories'),
    L('Telling stories (past continuous)', 'Contar histórias no passado', 'park', 'Colin+Vera', 'I was… when… / While we were… / Suddenly…', 'Story structure'),
    L('Detailed directions', 'Direções detalhadas', 'city', 'Cleo+Raj', 'Go straight / Turn… at the… / You can’t miss it', 'Landmarks'),
    L('News and events', 'Notícias e eventos', 'newsroom', 'Amy+Tessa', 'Did you hear about…? / Apparently… / I read that…', 'Sharing news'),
    L('Traditions and festivals', 'Tradições e festivais', 'fairground', 'Hana+Carlos', 'In my country… / People usually… / We celebrate…', 'Sharing traditions'),
    L('Small talk with strangers', 'Conversa informal com estranhos', 'busstop', 'Sam+Una', 'Lovely day, isn’t it? / Are you from here? / Have a nice day', 'Light conversation'),
    L('Real-Life Mission Day 12', 'Missão da unidade 12', 'plaza', 'Rosa+Diego+Hana', 'invite · share · tell · connect', 'Integrated mission: a cultural evening')]))
U.append((13, 'A2', 'A2 consolidation', [
    L('Planning a trip together', 'Planejar uma viagem juntos', 'office', 'Eva+Noah', 'Let’s… / We could… / What about…? / I’d rather…', 'Negotiating plans'),
    L('Workplace requests', 'Pedidos no trabalho', 'office', 'Raj+Pia', 'Could you…? / Would it be possible to…? / I’ll take care of…', 'Polite requests'),
    L('Online shopping and delivery', 'Compras online e entregas', 'bedroom', 'Zara+Elif', 'My order hasn’t arrived / Can I track…? / I’d like to change…', 'Delivery culture'),
    L('A short presentation', 'Uma apresentação curta', 'classroom', 'Mina+Ryo', 'Today I’m going to talk about… / First… / To sum up…', 'Presentation structure'),
    L('A2 situations review', 'Revisão de situações do A2', 'plaza', 'Ana+Tom+Maya', 'review of requests · plans · problems', 'Spaced review of all A2 patterns'),
    L('A2 Final Mission', 'Missão final do A2', 'airport', 'Mia+Ken+Eva', 'meet · plan · solve · negotiate', 'Integrated mission: a trip with a problem to solve')]))

if __name__ == '__main__':
    out, n = [], 0
    for un, lvl, name, ls in U:
        for k, l in enumerate(ls, 1):
            n += 1
            out.append(dict(n=n, unit=dict(n=un, k=k, of=len(ls), name=name), level=lvl, **l))
    os.makedirs(os.path.join(HERE, '..', 'data', 'v3'), exist_ok=True)
    json.dump(out, open(os.path.join(HERE, '..', 'data', 'v3', 'curriculum.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    from collections import Counter
    print('aulas:', len(out), Counter(x['level'] for x in out))
