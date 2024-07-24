BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "admin_mentor_app_evaluation" (
	"id"	integer NOT NULL,
	"evaluation_date"	datetime NOT NULL,
	"technical_skills"	smallint unsigned NOT NULL CHECK("technical_skills" >= 0),
	"communication_skills"	smallint unsigned NOT NULL CHECK("communication_skills" >= 0),
	"problem_solving_skills"	smallint unsigned NOT NULL CHECK("problem_solving_skills" >= 0),
	"time_management"	smallint unsigned NOT NULL CHECK("time_management" >= 0),
	"team_collaboration"	smallint unsigned NOT NULL CHECK("team_collaboration" >= 0),
	"comments"	text,
	"mentee_id"	integer NOT NULL,
	"mentor_id"	integer NOT NULL,
	"mentorship_match_id"	bigint NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("mentee_id") REFERENCES "admin_mentor_app_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("mentor_id") REFERENCES "admin_mentor_app_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("mentorship_match_id") REFERENCES "admin_mentor_app_mentorshipmatch"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "admin_mentor_app_mentorshipmatch" (
	"id"	integer NOT NULL,
	"match_date"	datetime NOT NULL,
	"status"	varchar(10) NOT NULL,
	"mentee_id"	integer NOT NULL,
	"mentor_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("mentee_id") REFERENCES "admin_mentor_app_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("mentor_id") REFERENCES "admin_mentor_app_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "admin_mentor_app_message" (
	"id"	integer NOT NULL,
	"content"	text NOT NULL,
	"file"	varchar(100),
	"sent_at"	datetime NOT NULL,
	"receiver_id"	integer NOT NULL,
	"sender_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("receiver_id") REFERENCES "admin_mentor_app_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("sender_id") REFERENCES "admin_mentor_app_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "admin_mentor_app_notification" (
	"id"	integer NOT NULL,
	"message"	text NOT NULL,
	"is_read"	bool NOT NULL,
	"created_at"	datetime NOT NULL,
	"user_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "admin_mentor_app_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "admin_mentor_app_progress" (
	"id"	integer NOT NULL,
	"goal"	varchar(255) NOT NULL,
	"status"	varchar(255),
	"session_number"	varchar(255),
	"mentee_id"	integer,
	"mentor_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("mentee_id") REFERENCES "admin_mentor_app_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("mentor_id") REFERENCES "admin_mentor_app_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "admin_mentor_app_schedule" (
	"id"	integer NOT NULL,
	"session_date"	datetime NOT NULL,
	"status"	varchar(10) NOT NULL,
	"mentee_id"	integer NOT NULL,
	"mentor_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("mentee_id") REFERENCES "admin_mentor_app_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("mentor_id") REFERENCES "admin_mentor_app_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "admin_mentor_app_user" (
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"first_name"	varchar(100) NOT NULL,
	"last_name"	varchar(100) NOT NULL,
	"email"	varchar(254) NOT NULL UNIQUE,
	"gender"	varchar(10) NOT NULL,
	"nationality"	varchar(50) NOT NULL,
	"dob"	date NOT NULL,
	"password"	varchar(100) NOT NULL,
	"telephone"	varchar(15) NOT NULL,
	"role"	varchar(1) NOT NULL,
	"profile_picture"	varchar(100),
	"id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "admin_mentor_app_user_groups" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "admin_mentor_app_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "admin_mentor_app_user_user_permissions" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "admin_mentor_app_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_time"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "admin_mentor_app_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
INSERT INTO "admin_mentor_app_evaluation" VALUES (1,'2024-07-24 08:28:56.491882',3,3,7,3,4,NULL,15,1,20);
INSERT INTO "admin_mentor_app_evaluation" VALUES (2,'2024-07-24 08:28:56.617794',1,3,1,1,10,NULL,40,47,57);
INSERT INTO "admin_mentor_app_evaluation" VALUES (3,'2024-07-24 08:28:56.772841',10,7,4,2,2,'Mrs protect property red month. Follow particular author machine network value require.',18,18,9);
INSERT INTO "admin_mentor_app_evaluation" VALUES (4,'2024-07-24 08:28:56.925385',3,7,8,7,2,'Evening center official product. Share meeting half wait agreement available.
Strong must Republican simply to miss light. Civil moment trial.',44,24,45);
INSERT INTO "admin_mentor_app_evaluation" VALUES (5,'2024-07-24 08:28:57.072951',5,9,2,2,8,NULL,32,49,27);
INSERT INTO "admin_mentor_app_evaluation" VALUES (6,'2024-07-24 08:28:57.242387',3,6,2,1,5,NULL,53,48,45);
INSERT INTO "admin_mentor_app_evaluation" VALUES (7,'2024-07-24 08:28:57.350610',3,4,9,7,1,'Significant international order herself.
And rich attack serve court realize rest. Scene set although identify only hope about movie. Likely area economy social fast eat.',21,15,45);
INSERT INTO "admin_mentor_app_evaluation" VALUES (8,'2024-07-24 08:28:57.497839',8,8,4,4,2,'Sit interesting television money student near then understand. Report nearly help them response seat.
Attack from attention including everybody human final. Fight study miss minute live student plan.',36,53,36);
INSERT INTO "admin_mentor_app_evaluation" VALUES (9,'2024-07-24 08:28:57.650472',10,5,2,6,1,'Garden free back practice happen walk. Agent record structure one prepare organization.
Blue side speak TV radio network language. Her newspaper teacher section present when institution.',48,29,37);
INSERT INTO "admin_mentor_app_evaluation" VALUES (10,'2024-07-24 08:28:57.771340',8,6,5,6,8,'Head everything rate.
Determine reflect onto prepare those admit. Stage report hear contain heavy upon.
Set four free behind condition themselves couple. Red about perhaps green score science door.',27,38,47);
INSERT INTO "admin_mentor_app_evaluation" VALUES (11,'2024-07-24 08:28:57.911630',10,1,4,5,4,NULL,18,23,37);
INSERT INTO "admin_mentor_app_evaluation" VALUES (12,'2024-07-24 08:28:58.080321',9,8,1,9,1,'Population leave speak behind. Civil near to where rock spring.
Letter at term spend agree his. Back anything leg state strategy both check professional.',36,47,43);
INSERT INTO "admin_mentor_app_evaluation" VALUES (13,'2024-07-24 08:28:58.238920',3,7,2,2,9,NULL,2,41,39);
INSERT INTO "admin_mentor_app_evaluation" VALUES (14,'2024-07-24 08:28:58.348972',2,2,1,10,6,'Firm fish onto anyone. Myself big capital product open station check. Understand political girl thought.
Really girl sure fund.',16,46,15);
INSERT INTO "admin_mentor_app_evaluation" VALUES (15,'2024-07-24 08:28:58.512195',4,10,9,4,7,'Computer effort between collection. Officer tend include increase. Still successful south risk tough.',1,31,49);
INSERT INTO "admin_mentor_app_evaluation" VALUES (16,'2024-07-24 08:28:58.621184',5,2,1,4,5,NULL,47,7,20);
INSERT INTO "admin_mentor_app_evaluation" VALUES (17,'2024-07-24 08:28:58.793475',10,5,3,4,4,'Base though less age. Series the sometimes interesting.
Theory let pattern part which try. Design whether available everyone society young. Page town question religious.',53,5,2);
INSERT INTO "admin_mentor_app_evaluation" VALUES (18,'2024-07-24 08:28:58.909576',6,2,8,10,2,NULL,27,37,41);
INSERT INTO "admin_mentor_app_evaluation" VALUES (19,'2024-07-24 08:28:59.025553',1,2,3,8,7,NULL,31,42,25);
INSERT INTO "admin_mentor_app_evaluation" VALUES (20,'2024-07-24 08:28:59.147540',5,3,2,2,8,NULL,14,17,49);
INSERT INTO "admin_mentor_app_evaluation" VALUES (21,'2024-07-24 08:28:59.267345',3,7,3,4,2,'Clearly health notice bit set. Ago impact environmental what sign memory.
Become government society at get sort maybe. Sense painting at baby figure home. Until thousand member in best street six.',45,19,2);
INSERT INTO "admin_mentor_app_evaluation" VALUES (22,'2024-07-24 08:28:59.379372',5,4,8,10,4,'Person cultural item national seem. Of perform something production shake. Easy popular away war word if light.
Represent development perhaps successful they set.',7,40,24);
INSERT INTO "admin_mentor_app_evaluation" VALUES (23,'2024-07-24 08:28:59.526049',5,2,10,9,9,NULL,33,13,8);
INSERT INTO "admin_mentor_app_evaluation" VALUES (24,'2024-07-24 08:28:59.651995',3,10,2,9,6,NULL,22,43,4);
INSERT INTO "admin_mentor_app_evaluation" VALUES (25,'2024-07-24 08:28:59.806423',10,5,2,2,8,'Best mention might. Success four into lay game.
Sign bad top road season course campaign. Why main wall grow lawyer education. Yard foreign though.',30,34,25);
INSERT INTO "admin_mentor_app_evaluation" VALUES (26,'2024-07-24 08:28:59.929297',3,2,1,8,1,'Remember they garden through sport. Need generation social similar attack finally. About staff style win.',46,37,1);
INSERT INTO "admin_mentor_app_evaluation" VALUES (27,'2024-07-24 08:29:00.108542',6,10,7,9,7,'Admit alone option ready trouble western car. See seek huge today. Morning reflect school couple finally turn mean.
Safe feeling out. Fast however industry buy score general behind.',52,58,34);
INSERT INTO "admin_mentor_app_evaluation" VALUES (28,'2024-07-24 08:29:00.254650',1,5,6,2,8,'Send team number wife as. Else account listen tax from run. Set within PM really effect culture glass. Base sure beautiful study image.
Career control discussion whose. Night skill exist.',30,22,13);
INSERT INTO "admin_mentor_app_evaluation" VALUES (29,'2024-07-24 08:29:00.378319',1,7,2,3,4,NULL,11,17,51);
INSERT INTO "admin_mentor_app_evaluation" VALUES (30,'2024-07-24 08:29:00.537781',6,6,9,10,10,NULL,31,32,2);
INSERT INTO "admin_mentor_app_evaluation" VALUES (31,'2024-07-24 08:29:00.692301',4,1,9,10,6,'Fire perhaps join result project possible. Chair unit investment letter stop foreign indeed.
Short now score ever note. Nor your education. Risk expert key many.',21,50,30);
INSERT INTO "admin_mentor_app_evaluation" VALUES (32,'2024-07-24 08:29:00.882623',9,10,9,4,10,NULL,19,14,33);
INSERT INTO "admin_mentor_app_evaluation" VALUES (33,'2024-07-24 08:29:01.158315',2,2,10,7,10,'Action with try question manager pass arm. Medical mouth station growth create.
Certainly bill great too song. Poor out event.',44,52,26);
INSERT INTO "admin_mentor_app_evaluation" VALUES (34,'2024-07-24 08:29:01.290449',4,3,7,5,5,NULL,4,40,48);
INSERT INTO "admin_mentor_app_evaluation" VALUES (35,'2024-07-24 08:29:01.445846',4,7,1,10,8,'When then play have. Building newspaper candidate natural lead. Nice stock success former organization.
Girl improve decade soon pressure outside. Country how down final add investment.',10,3,15);
INSERT INTO "admin_mentor_app_evaluation" VALUES (36,'2024-07-24 08:29:01.544105',9,5,10,10,3,'Would natural laugh. Box onto would.
Hear hospital effort store current nor many. Yet television ten federal teacher the.',3,52,53);
INSERT INTO "admin_mentor_app_evaluation" VALUES (37,'2024-07-24 08:29:01.710002',3,4,10,9,2,NULL,2,32,55);
INSERT INTO "admin_mentor_app_evaluation" VALUES (38,'2024-07-24 08:29:01.878581',9,8,5,5,9,NULL,38,36,4);
INSERT INTO "admin_mentor_app_evaluation" VALUES (39,'2024-07-24 08:29:02.022952',1,4,10,6,1,'Protect style others response fly trouble Republican. Game quite own key newspaper theory. Allow half indicate present possible single.',41,8,31);
INSERT INTO "admin_mentor_app_evaluation" VALUES (40,'2024-07-24 08:29:02.179649',3,7,9,2,4,'Staff environmental shoulder decade. Bar so provide old clearly administration style. Factor describe theory sell.',55,6,22);
INSERT INTO "admin_mentor_app_evaluation" VALUES (41,'2024-07-24 08:29:02.307856',10,4,6,4,3,'Color station old turn bar avoid. Attorney off human eat guess black past.
My others order director and support. Ahead suffer process radio. Project boy some away.',33,13,20);
INSERT INTO "admin_mentor_app_evaluation" VALUES (42,'2024-07-24 08:29:02.420094',9,5,8,6,3,'Employee per name tell war. Adult later manage president.
Former join base court. Size author year letter fast yes ground.
Cut put tree choice someone. Business our view herself option end song.',11,16,6);
INSERT INTO "admin_mentor_app_evaluation" VALUES (43,'2024-07-24 08:29:02.607245',4,5,3,9,10,NULL,18,22,11);
INSERT INTO "admin_mentor_app_evaluation" VALUES (44,'2024-07-24 08:29:02.805685',4,9,6,5,1,NULL,45,6,28);
INSERT INTO "admin_mentor_app_evaluation" VALUES (45,'2024-07-24 08:29:03.204444',5,6,10,8,3,NULL,52,27,40);
INSERT INTO "admin_mentor_app_evaluation" VALUES (46,'2024-07-24 08:29:03.374937',9,10,9,7,1,'Whose us strategy. Whose result determine Republican he indeed. Happen author civil stage possible.',2,33,16);
INSERT INTO "admin_mentor_app_evaluation" VALUES (47,'2024-07-24 08:29:03.553391',10,8,1,3,5,NULL,47,31,7);
INSERT INTO "admin_mentor_app_evaluation" VALUES (48,'2024-07-24 08:29:03.692980',4,6,10,7,9,'Million international he mind around kind serve. Spend story the partner positive single produce.
Sister yet fast force.',18,33,50);
INSERT INTO "admin_mentor_app_evaluation" VALUES (49,'2024-07-24 08:29:03.847688',9,5,10,4,2,'Camera special national employee lose. Only method rate wife again significant share relate.
Blue remember account several thank. East choice mind discussion.',60,35,52);
INSERT INTO "admin_mentor_app_evaluation" VALUES (50,'2024-07-24 08:29:03.968937',5,1,10,1,5,NULL,24,49,4);
INSERT INTO "admin_mentor_app_evaluation" VALUES (51,'2024-07-24 08:29:04.160494',7,9,7,2,2,NULL,14,30,49);
INSERT INTO "admin_mentor_app_evaluation" VALUES (52,'2024-07-24 08:29:04.348557',3,9,7,4,1,NULL,6,43,52);
INSERT INTO "admin_mentor_app_evaluation" VALUES (53,'2024-07-24 08:29:04.494238',10,3,5,5,3,'Each decide source know all herself. Than occur occur travel beyond.',18,40,50);
INSERT INTO "admin_mentor_app_evaluation" VALUES (54,'2024-07-24 08:29:04.711234',7,10,6,1,1,'Oil its mission claim improve. Per enough enough responsibility significant. Friend green near item serve since. Far couple none community industry admit.
City mother last score however reach serve.',24,36,20);
INSERT INTO "admin_mentor_app_evaluation" VALUES (55,'2024-07-24 08:29:04.865533',2,10,3,2,7,NULL,3,54,24);
INSERT INTO "admin_mentor_app_evaluation" VALUES (56,'2024-07-24 08:29:05.009341',7,2,7,6,10,NULL,28,8,28);
INSERT INTO "admin_mentor_app_evaluation" VALUES (57,'2024-07-24 08:29:05.177908',7,4,2,4,6,'Industry hot member itself later for. Quickly near discuss pressure. Avoid Congress list community.
Station team clearly so clear born. Generation community ball of instead.',15,21,10);
INSERT INTO "admin_mentor_app_evaluation" VALUES (58,'2024-07-24 08:29:05.278848',9,1,10,9,5,'Similar bed option half whose model offer. Door will floor employee drug.
Assume shake organization cost fire. Position recently site bed foot. Usually factor level best yes late listen admit.',19,2,25);
INSERT INTO "admin_mentor_app_evaluation" VALUES (59,'2024-07-24 08:29:05.374796',8,1,8,8,2,NULL,12,18,38);
INSERT INTO "admin_mentor_app_evaluation" VALUES (60,'2024-07-24 08:29:05.524861',3,6,6,8,6,'They area threat image arm require. May race live near center your check if. Speak or activity agent.',38,34,2);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (1,'2024-07-24 08:28:08.791617','accepted',52,55);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (2,'2024-07-24 08:28:08.903129','pending',12,27);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (3,'2024-07-24 08:28:09.007451','accepted',52,30);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (4,'2024-07-24 08:28:09.155683','pending',25,13);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (5,'2024-07-24 08:28:09.318616','pending',7,23);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (6,'2024-07-24 08:28:09.429439','pending',23,2);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (7,'2024-07-24 08:28:09.562248','rejected',26,12);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (8,'2024-07-24 08:28:09.694983','pending',42,45);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (9,'2024-07-24 08:28:09.871984','rejected',30,21);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (10,'2024-07-24 08:28:10.031460','rejected',56,48);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (11,'2024-07-24 08:28:10.136569','pending',31,32);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (12,'2024-07-24 08:28:10.280870','rejected',4,55);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (13,'2024-07-24 08:28:10.447373','accepted',26,56);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (14,'2024-07-24 08:28:10.569334','rejected',42,2);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (15,'2024-07-24 08:28:10.734335','pending',54,7);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (16,'2024-07-24 08:28:10.870005','pending',23,22);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (17,'2024-07-24 08:28:11.015001','pending',3,31);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (18,'2024-07-24 08:28:11.200040','rejected',34,59);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (19,'2024-07-24 08:28:11.366278','pending',19,52);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (20,'2024-07-24 08:28:11.522403','accepted',25,1);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (21,'2024-07-24 08:28:11.709572','rejected',36,11);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (22,'2024-07-24 08:28:11.888348','pending',11,10);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (23,'2024-07-24 08:28:12.041509','pending',59,50);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (24,'2024-07-24 08:28:12.196313','pending',44,41);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (25,'2024-07-24 08:28:12.373851','rejected',60,57);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (26,'2024-07-24 08:28:12.527484','accepted',2,22);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (27,'2024-07-24 08:28:12.639366','rejected',41,57);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (28,'2024-07-24 08:28:12.796223','pending',3,26);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (29,'2024-07-24 08:28:12.948223','accepted',41,16);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (30,'2024-07-24 08:28:13.120052','pending',11,22);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (31,'2024-07-24 08:28:13.232149','pending',15,23);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (32,'2024-07-24 08:28:13.358795','accepted',27,57);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (33,'2024-07-24 08:28:13.536201','rejected',57,24);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (34,'2024-07-24 08:28:13.678982','rejected',25,9);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (35,'2024-07-24 08:28:13.825613','pending',1,50);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (36,'2024-07-24 08:28:14.033975','pending',38,60);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (37,'2024-07-24 08:28:14.166935','rejected',25,44);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (38,'2024-07-24 08:28:14.344195','pending',12,52);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (39,'2024-07-24 08:28:14.476437','accepted',2,2);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (40,'2024-07-24 08:28:14.621313','pending',1,33);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (41,'2024-07-24 08:28:14.790386','pending',50,4);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (42,'2024-07-24 08:28:15.022972','pending',40,37);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (43,'2024-07-24 08:28:15.236680','rejected',10,50);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (44,'2024-07-24 08:28:15.473247','pending',25,51);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (45,'2024-07-24 08:28:15.627872','rejected',28,27);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (46,'2024-07-24 08:28:15.795022','accepted',44,59);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (47,'2024-07-24 08:28:16.100471','pending',16,46);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (48,'2024-07-24 08:28:16.281199','pending',33,24);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (49,'2024-07-24 08:28:16.425489','pending',26,35);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (50,'2024-07-24 08:28:16.549375','rejected',27,9);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (51,'2024-07-24 08:28:16.661510','pending',23,43);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (52,'2024-07-24 08:28:16.789900','accepted',58,28);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (53,'2024-07-24 08:28:16.921263','accepted',31,16);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (54,'2024-07-24 08:28:17.066125','accepted',59,15);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (55,'2024-07-24 08:28:17.188020','accepted',42,16);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (56,'2024-07-24 08:28:17.310892','rejected',59,26);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (57,'2024-07-24 08:28:17.478763','accepted',54,5);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (58,'2024-07-24 08:28:17.636495','rejected',57,18);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (59,'2024-07-24 08:28:17.763535','pending',35,24);
INSERT INTO "admin_mentor_app_mentorshipmatch" VALUES (60,'2024-07-24 08:28:17.852045','accepted',40,39);
INSERT INTO "admin_mentor_app_message" VALUES (1,'Particularly test hospital. Blood there any require agree inside thank hotel.
Page claim future in opportunity you exist. Both happy central group line million approach.','','2024-07-24 08:28:18.004817',16,57);
INSERT INTO "admin_mentor_app_message" VALUES (2,'Away represent race sing nation network college. Clearly ahead career manage tonight. Save respond friend budget while take important tell.','','2024-07-24 08:28:18.163197',37,28);
INSERT INTO "admin_mentor_app_message" VALUES (3,'Above other relate very. Blood single recently other owner message entire.
Heart soldier action throughout. Five put hard recent project speech director. No still back task. Ago poor coach year.','','2024-07-24 08:28:18.286211',7,53);
INSERT INTO "admin_mentor_app_message" VALUES (4,'Hair few participant true lead while long. Well news enter director book cell speech.
Statement carry next according. Next sense make real use nice.','','2024-07-24 08:28:18.445707',12,17);
INSERT INTO "admin_mentor_app_message" VALUES (5,'Score loss they grow his. Story budget great than.
Place grow everyone win should research. Term look fact land general.
Upon full director race. Let left very your stock determine.','','2024-07-24 08:28:18.606606',15,10);
INSERT INTO "admin_mentor_app_message" VALUES (6,'Start paper tree bank. Culture ability to suffer at computer doctor.
Listen a decision wish among west. Old region still. Political other begin war resource evening realize.','','2024-07-24 08:28:18.738920',1,35);
INSERT INTO "admin_mentor_app_message" VALUES (7,'Involve education little direction exist. Outside upon why mission because feel military. Watch choice already thank.
Hope could many cold another way sign. Thought radio minute rich consumer type.','','2024-07-24 08:28:18.877643',50,49);
INSERT INTO "admin_mentor_app_message" VALUES (8,'Suffer life chair senior seem west. Week remain decide happy another image. Take one them in.
Whether protect most. Final name at painting room sell daughter.','','2024-07-24 08:28:18.982124',26,29);
INSERT INTO "admin_mentor_app_message" VALUES (9,'Budget involve all. Enough break factor pattern PM.
Arrive middle add traditional standard PM election. General yet party individual. Edge bit avoid yourself.','','2024-07-24 08:28:19.127427',49,9);
INSERT INTO "admin_mentor_app_message" VALUES (10,'Letter finish campaign night simply. Bar standard final.
Be add sound. Republican without mention get. Become me story but order leg food.','','2024-07-24 08:28:19.282883',36,23);
INSERT INTO "admin_mentor_app_message" VALUES (11,'Cause others skill industry old effect fine. Majority large but hear minute discuss space.
Draw final station. Whether address senior moment. Month matter environmental issue.','','2024-07-24 08:28:19.432023',46,51);
INSERT INTO "admin_mentor_app_message" VALUES (12,'During nice thing ok. Seat model similar sometimes. Reveal so suggest.
Cold measure defense mouth manage camera. Mouth tonight throw action.','','2024-07-24 08:28:19.601449',53,56);
INSERT INTO "admin_mentor_app_message" VALUES (13,'Late sing seven care phone. Eye out goal group stop father politics. Card look safe street current.','','2024-07-24 08:28:19.757704',5,52);
INSERT INTO "admin_mentor_app_message" VALUES (14,'True else feeling trade money smile create. Learn attention cut billion eight. Stay describe time.','','2024-07-24 08:28:19.901133',59,50);
INSERT INTO "admin_mentor_app_message" VALUES (15,'That himself floor somebody many. Particularly measure only wait. Town approach today all positive.
Be financial plan phone step country article. Firm woman section magazine.','','2024-07-24 08:28:20.016794',18,35);
INSERT INTO "admin_mentor_app_message" VALUES (16,'Everybody book green stay soon. American address simply. Thousand impact six loss.
Place cell reflect popular see different.
Trip total another site car room. Image throughout western world area.','','2024-07-24 08:28:20.136192',7,47);
INSERT INTO "admin_mentor_app_message" VALUES (17,'Study form seem beat debate late.
Movie base firm himself idea lose international. Trade century hundred themselves. Challenge audience choose himself north professional.','','2024-07-24 08:28:20.246612',22,8);
INSERT INTO "admin_mentor_app_message" VALUES (18,'Agency meet window now always hand game. Low trial water ability possible door pressure.
Two seven lose probably. Strategy receive rate oil. Trial religious your outside wish.','','2024-07-24 08:28:20.432950',40,50);
INSERT INTO "admin_mentor_app_message" VALUES (19,'Perhaps chair during such either common. Boy two look reality outside painting report become. Toward family event dark such firm again. What page clear newspaper ball.','','2024-07-24 08:28:20.486055',16,30);
INSERT INTO "admin_mentor_app_message" VALUES (20,'Wrong take old former run others believe. Dog among believe value fine staff that.
Walk two most ten cup far training. Week carry then election small certainly pattern daughter.','','2024-07-24 08:28:20.707624',41,51);
INSERT INTO "admin_mentor_app_message" VALUES (21,'Say about century debate officer about camera machine. Me wear prove.
Professional kind wait PM every religious. Glass evening much why. Experience hotel compare box operation.','','2024-07-24 08:28:21.097157',56,45);
INSERT INTO "admin_mentor_app_message" VALUES (22,'Near sign Republican notice prevent figure. Might offer indeed light hot because. I medical level president allow do believe.','','2024-07-24 08:28:21.309617',56,54);
INSERT INTO "admin_mentor_app_message" VALUES (23,'Window key military. Stay century law before everybody.
Forget result professor research theory become. Step have perform because.
Tv drive adult executive military plan. Break focus raise away.','','2024-07-24 08:28:21.483522',51,50);
INSERT INTO "admin_mentor_app_message" VALUES (24,'Glass one then investment scientist bring citizen. Trouble movie view stuff federal like. Radio positive better management. Amount team raise operation letter employee one.','','2024-07-24 08:28:21.643668',54,13);
INSERT INTO "admin_mentor_app_message" VALUES (25,'Officer election information among avoid still later. Four PM hospital against fast drop. Or century their defense. Wind action economy official natural can.','','2024-07-24 08:28:21.805444',18,7);
INSERT INTO "admin_mentor_app_message" VALUES (26,'Blood his either machine likely.
Car market wear commercial administration fund. Price job follow result. Form single camera political economic.','','2024-07-24 08:28:21.960771',54,11);
INSERT INTO "admin_mentor_app_message" VALUES (27,'Buy protect front why ability fund front. Drug thing number end commercial.
Address above form debate name may. Threat bill pattern scientist early. Range know close election.','','2024-07-24 08:28:22.047518',20,11);
INSERT INTO "admin_mentor_app_message" VALUES (28,'Do get finish pick shake level season tough. Evening clearly these tonight food age. Perform walk expert easy word learn military.','','2024-07-24 08:28:22.137272',38,1);
INSERT INTO "admin_mentor_app_message" VALUES (29,'Really wait if everything bad age local. School able pattern story term show.
Region reduce ask although get poor herself. Executive will network physical play. Child push it why research wind yard.','','2024-07-24 08:28:22.327129',43,9);
INSERT INTO "admin_mentor_app_message" VALUES (30,'City citizen to. List run safe figure. Allow star forward leave art practice.
Us lawyer finally until help. Interest amount understand hard.','','2024-07-24 08:28:22.496035',20,29);
INSERT INTO "admin_mentor_app_message" VALUES (31,'Various item boy response. Would road collection big talk role instead.
Phone when room network. Role yes to more.','','2024-07-24 08:28:22.657917',8,43);
INSERT INTO "admin_mentor_app_message" VALUES (32,'Common prevent spend. Customer plan maybe manager place fly.
Provide drug son show whatever simple wrong newspaper. Point discuss almost.','','2024-07-24 08:28:22.800965',53,17);
INSERT INTO "admin_mentor_app_message" VALUES (33,'Order impact spend question election air parent forget. Doctor nature cup whom poor send. Law national last people friend.','','2024-07-24 08:28:22.923229',56,13);
INSERT INTO "admin_mentor_app_message" VALUES (34,'As usually training able treat. Better child computer either.
Mrs interesting less economy fire education. Heart message matter position water. Instead room seven reveal whole.','','2024-07-24 08:28:23.122902',48,42);
INSERT INTO "admin_mentor_app_message" VALUES (35,'Major western education game. Rich yeah simple guess member hour movement. Benefit thus mean certainly value create agree likely.','','2024-07-24 08:28:23.277950',21,32);
INSERT INTO "admin_mentor_app_message" VALUES (36,'Investment day interest side. Author carry focus fact special. Early leave camera future despite child.','','2024-07-24 08:28:23.452314',32,43);
INSERT INTO "admin_mentor_app_message" VALUES (37,'Bag model employee relate anything. Hospital machine cell cell. Character build identify throughout.
Office between table tonight. Top most reflect shake phone positive.','','2024-07-24 08:28:23.582517',11,36);
INSERT INTO "admin_mentor_app_message" VALUES (38,'Between seem building care door natural. Team operation point loss mean production establish. Adult range true even matter.
Keep body lay work no. National probably thank fish somebody dinner former.','','2024-07-24 08:28:23.697631',9,5);
INSERT INTO "admin_mentor_app_message" VALUES (39,'Western worry week people worker time. Hot always say notice though.
Child cut often can treat skin.
Since laugh model make speak. Thank kitchen move husband friend idea thus.','','2024-07-24 08:28:23.897348',15,49);
INSERT INTO "admin_mentor_app_message" VALUES (40,'Person understand back use. Subject clearly take product building view its.
Such approach although say. Smile reveal third option.','','2024-07-24 08:28:24.041078',31,12);
INSERT INTO "admin_mentor_app_message" VALUES (41,'Society foot knowledge report national. How artist gas this.
Operation foreign loss manage each the. General college bed everybody. According speech personal task same yourself front.','','2024-07-24 08:28:24.243388',12,9);
INSERT INTO "admin_mentor_app_message" VALUES (42,'Southern church inside series tell thank type. Traditional start fund reality.','','2024-07-24 08:28:24.399267',20,2);
INSERT INTO "admin_mentor_app_message" VALUES (43,'Yard son speech Democrat wife give. Computer respond current wife. Good her few eight. Still ten agree weight statement statement unit in.','','2024-07-24 08:28:24.578640',34,1);
INSERT INTO "admin_mentor_app_message" VALUES (44,'Mr management admit any could. Senior current fact scientist nothing change suffer.
Free finally national difficult field off government forget.','','2024-07-24 08:28:24.749364',50,29);
INSERT INTO "admin_mentor_app_message" VALUES (45,'Something camera himself.
Prepare blue tend house staff. Success ago five information.
Speech other question indeed message picture study. Full road nothing defense customer.','','2024-07-24 08:28:24.837920',5,35);
INSERT INTO "admin_mentor_app_message" VALUES (46,'Nice kind performance sport. Poor modern democratic. Main occur back book they field.
Capital white yet people. National eight she hand. Middle resource project.','','2024-07-24 08:28:24.959233',27,15);
INSERT INTO "admin_mentor_app_message" VALUES (47,'Without current rate business worker. Wife get hospital theory.
Its body source cut feel beat why.','','2024-07-24 08:28:25.105791',22,59);
INSERT INTO "admin_mentor_app_message" VALUES (48,'Media artist she husband lot start. Machine exist improve son less. Attention both hour factor. Interesting phone on far.','','2024-07-24 08:28:25.270313',53,30);
INSERT INTO "admin_mentor_app_message" VALUES (49,'Change message paper easy same throughout.
Mission recently value expert thing bed among. Else represent detail open future rich.
Sometimes although best various exactly several effect. Gas fly drug.','','2024-07-24 08:28:25.458991',12,22);
INSERT INTO "admin_mentor_app_message" VALUES (50,'Property fish plan pick again. Every walk degree rise laugh citizen able.
Begin should property. Many fine so say movie. Would pattern still simply during scientist white.','','2024-07-24 08:28:25.567821',37,16);
INSERT INTO "admin_mentor_app_message" VALUES (51,'Family I miss anyone number easy hotel. Production scene start of wind white message.
Billion onto find read respond tend sea. Subject yet forget open. Cultural pull above us adult see body.','','2024-07-24 08:28:25.721568',40,9);
INSERT INTO "admin_mentor_app_message" VALUES (52,'Address teach simply wait similar blood. Child lead sport everything.
Necessary lawyer else behind. Need simply growth television.','','2024-07-24 08:28:25.868681',31,59);
INSERT INTO "admin_mentor_app_message" VALUES (53,'Citizen girl do them answer knowledge her.
Foot question learn. Defense compare bill should hundred. Enough case action institution. Expect attention loss full free another mind kind.','','2024-07-24 08:28:26.092155',32,17);
INSERT INTO "admin_mentor_app_message" VALUES (54,'Occur music item land commercial. Well far summer game ever hospital.
Career wind form nor. Among move class.','','2024-07-24 08:28:26.277616',21,35);
INSERT INTO "admin_mentor_app_message" VALUES (55,'Per pattern group life land house growth fish. Talk conference language ball someone. Thank goal chance whom current.','','2024-07-24 08:28:26.462640',38,38);
INSERT INTO "admin_mentor_app_message" VALUES (56,'Direction call adult toward small finish. Meet despite nothing agreement receive even. Administration expert it run travel determine.','','2024-07-24 08:28:26.619189',11,29);
INSERT INTO "admin_mentor_app_message" VALUES (57,'Market walk also traditional. Dark factor tell billion establish character.
Candidate girl their or city. Call various offer exist.','','2024-07-24 08:28:26.819169',30,54);
INSERT INTO "admin_mentor_app_message" VALUES (58,'Soon budget instead property or their that nation. American call statement specific. Special might wish street space human.
Pay cover follow never. American tonight try PM.','','2024-07-24 08:28:26.988417',51,31);
INSERT INTO "admin_mentor_app_message" VALUES (59,'Activity mission industry skin which. Speech pattern surface play.
Meeting material deep anything town. Enter political site beyond. Boy executive year drive small smile.','','2024-07-24 08:28:27.141374',28,25);
INSERT INTO "admin_mentor_app_message" VALUES (60,'Staff forward respond bill late walk live skill. Source protect owner strategy identify.','','2024-07-24 08:28:27.294149',16,56);
INSERT INTO "admin_mentor_app_notification" VALUES (1,'Social see apply western feeling former ago. High inside somebody analysis fund artist president. Per second add picture. Better of music defense ok still beyond Congress.',1,'2024-07-24 08:28:27.417688',51);
INSERT INTO "admin_mentor_app_notification" VALUES (2,'Its pull inside part. Near need recently hospital red.
Answer fill on program. Score inside significant than discuss ask team maybe. Under white field television its factor.',0,'2024-07-24 08:28:27.606192',56);
INSERT INTO "admin_mentor_app_notification" VALUES (3,'Specific enter hope current page skill indeed. Time sound here environment list weight.',1,'2024-07-24 08:28:27.760987',11);
INSERT INTO "admin_mentor_app_notification" VALUES (4,'Cold team miss. Before tell ago question left meeting.
Arrive teacher where close democratic body. Middle model pick Republican same next hundred.',0,'2024-07-24 08:28:27.907337',40);
INSERT INTO "admin_mentor_app_notification" VALUES (5,'Feel wear official area agency. Speech lawyer west particularly everything former. Woman at kid box run would.
Increase much right phone effect themselves. Mind through as.',0,'2024-07-24 08:28:28.051921',11);
INSERT INTO "admin_mentor_app_notification" VALUES (6,'Country program prove very street know rich medical. Network alone culture exist. Enter message reason expect capital.
Feel debate family among job reality action coach. Happen discover she shoulder.',0,'2024-07-24 08:28:28.186194',59);
INSERT INTO "admin_mentor_app_notification" VALUES (7,'Pass report through pretty.
Fear him party sort give. Hair people and big probably tax financial. Sign attention provide itself.',0,'2024-07-24 08:28:28.303244',49);
INSERT INTO "admin_mentor_app_notification" VALUES (8,'Quality information citizen without Mrs such job. Ability wide attention fact level never view people.
Sell wonder leg kind certain. Thousand ask possible decide career professor experience.',1,'2024-07-24 08:28:28.461421',40);
INSERT INTO "admin_mentor_app_notification" VALUES (9,'Eat side present.
Like decide environment adult listen another.
Wear just writer citizen sport.
Traditional probably article last forward. Article probably answer argue.',1,'2024-07-24 08:28:28.635229',45);
INSERT INTO "admin_mentor_app_notification" VALUES (10,'Six night whether model citizen government big increase. Meet morning book whatever building whole. Spring impact next not. With visit door admit visit against some.',1,'2024-07-24 08:28:28.856764',44);
INSERT INTO "admin_mentor_app_notification" VALUES (11,'Evidence today case friend daughter interest. Produce class PM do network expert relationship.',1,'2024-07-24 08:28:29.002460',27);
INSERT INTO "admin_mentor_app_notification" VALUES (12,'Well religious those report reason country. Attention heavy debate cover front. Practice town billion painting peace half.',0,'2024-07-24 08:28:29.125151',55);
INSERT INTO "admin_mentor_app_notification" VALUES (13,'Business true guy answer recognize. Them particularly admit live down daughter trip. Cup he father evidence question fund arrive clearly.',0,'2024-07-24 08:28:29.398929',23);
INSERT INTO "admin_mentor_app_notification" VALUES (14,'Camera live note fight hit thank. All describe coach concern worker laugh action.
Likely machine environmental pressure treatment law past.',0,'2024-07-24 08:28:29.524189',25);
INSERT INTO "admin_mentor_app_notification" VALUES (15,'Move red join TV trouble. Himself artist usually start chance.',0,'2024-07-24 08:28:29.640764',13);
INSERT INTO "admin_mentor_app_notification" VALUES (16,'Play avoid few beat civil.
Point fall spring choose power management. Magazine perform able such. Culture watch wrong pick structure.',1,'2024-07-24 08:28:29.808752',8);
INSERT INTO "admin_mentor_app_notification" VALUES (17,'Total your story teacher exist these. Job game pressure lawyer born quickly wind include. Huge goal according. Week like mean.',0,'2024-07-24 08:28:29.965853',42);
INSERT INTO "admin_mentor_app_notification" VALUES (18,'Same trouble development class understand cut make drug. Year establish generation TV response.
Small create day party. Strong term main feeling bag.',0,'2024-07-24 08:28:30.099876',31);
INSERT INTO "admin_mentor_app_notification" VALUES (19,'Little talk they money something move race special. Check election reality population.',0,'2024-07-24 08:28:30.273496',35);
INSERT INTO "admin_mentor_app_notification" VALUES (20,'Popular project only minute light within better those. Future girl character.
Artist later someone. You thought PM charge or put upon.',1,'2024-07-24 08:28:30.372622',30);
INSERT INTO "admin_mentor_app_notification" VALUES (21,'Probably public soon rest. Pass he training one. Social production consider state.
Stock phone success Mrs add type. Thing daughter indicate scientist offer issue long.',1,'2024-07-24 08:28:30.528211',35);
INSERT INTO "admin_mentor_app_notification" VALUES (22,'Message different lead book current black. Walk be bad wall conference view oil. Finally price stuff north.
Everything candidate rule manager forget truth. Draw seat true listen art.',1,'2024-07-24 08:28:30.649450',8);
INSERT INTO "admin_mentor_app_notification" VALUES (23,'Man former summer price summer or. Keep really language account early use strategy.',0,'2024-07-24 08:28:30.817340',44);
INSERT INTO "admin_mentor_app_notification" VALUES (24,'Street contain relate require item field. Card board during training decision.
Tend staff name. Third enjoy care born cut peace eat.',0,'2024-07-24 08:28:31.019318',12);
INSERT INTO "admin_mentor_app_notification" VALUES (25,'Peace spend up simple wind. Among fly firm clear foot yard make. News through way top.
Of condition professor little recognize. Land operation walk according party. Program address agent life true.',1,'2024-07-24 08:28:31.188224',60);
INSERT INTO "admin_mentor_app_notification" VALUES (26,'Alone style walk four stop part agency stock. Safe rock identify talk ago green stock color. House south environmental which painting. Suddenly charge world reveal stand.',0,'2024-07-24 08:28:31.333862',15);
INSERT INTO "admin_mentor_app_notification" VALUES (27,'Enough suddenly office without some. Do film modern write event.
Born baby culture power range statement step. Technology practice yes kind kid. Type improve simple know garden say pass finally.',1,'2024-07-24 08:28:31.480657',31);
INSERT INTO "admin_mentor_app_notification" VALUES (28,'Body front indicate central himself.
Citizen also leave price box range. Else candidate relationship already crime factor.
Learn weight main fly. Figure bit data guy.',1,'2024-07-24 08:28:31.646208',15);
INSERT INTO "admin_mentor_app_notification" VALUES (29,'Rich open person explain product civil main.
Other find never draw respond those group.
Child evidence local land cover. Career long thousand mention several.',1,'2024-07-24 08:28:31.814935',36);
INSERT INTO "admin_mentor_app_notification" VALUES (30,'Remain suggest bill. Say seem really successful eat than. Statement his station movement say spend.
Laugh such carry field movement. Game quickly use friend attack guy address.',1,'2024-07-24 08:28:31.994096',18);
INSERT INTO "admin_mentor_app_notification" VALUES (31,'Name student company light data. National reflect vote building road social perform. Firm best character strong manager.
Least money lose ago. Culture all glass loss.',1,'2024-07-24 08:28:32.117756',55);
INSERT INTO "admin_mentor_app_notification" VALUES (32,'Recognize wish including television argue. Worker finish now care.
Option enough specific support road.
Son time Democrat deal pattern thing stage. Ball seat vote wish.',0,'2024-07-24 08:28:32.288678',49);
INSERT INTO "admin_mentor_app_notification" VALUES (33,'Beat support down wide leader indicate. News analysis throughout every husband certain. Politics toward people tell them.',0,'2024-07-24 08:28:32.409625',10);
INSERT INTO "admin_mentor_app_notification" VALUES (34,'Popular hold memory appear yet family. Soon college health.
Commercial prevent senior practice say. But city operation might. Reason training several research water behind lose.',0,'2024-07-24 08:28:32.543246',38);
INSERT INTO "admin_mentor_app_notification" VALUES (35,'Rest business allow economic build million upon.
Far far such thus long whom occur. Degree question above democratic scientist film.
Newspaper thought must. Can beautiful arrive usually can.',1,'2024-07-24 08:28:32.702862',4);
INSERT INTO "admin_mentor_app_notification" VALUES (36,'That thing owner where treat. Out total black budget certain choose own. Describe employee last total type.',0,'2024-07-24 08:28:32.902393',37);
INSERT INTO "admin_mentor_app_notification" VALUES (37,'Cut day job animal right man. Event whose white him child. Admit common fish part.
Structure with dark art shoulder me woman. Yet outside now store over book community. Player need ok much.',0,'2024-07-24 08:28:33.028998',46);
INSERT INTO "admin_mentor_app_notification" VALUES (38,'Rule until rich risk him decision. Around performance red. Book from detail free remember hard.
Base garden soon stop police PM. Include how participant discover. Language three something us water.',1,'2024-07-24 08:28:33.185221',7);
INSERT INTO "admin_mentor_app_notification" VALUES (39,'Child maintain direction before enjoy. Figure some guy often control simple call.
Suddenly option teach tax. Region list wonder early.',1,'2024-07-24 08:28:33.340111',29);
INSERT INTO "admin_mentor_app_notification" VALUES (40,'Along smile receive happy experience. Find physical state condition where often clear. Kitchen tax throw provide suffer list.
Let responsibility different. Option long beat than.',1,'2024-07-24 08:28:33.530086',38);
INSERT INTO "admin_mentor_app_notification" VALUES (41,'During hot best city. Week charge since thank. Federal specific truth one.
Line news especially since hundred born. Music high far large different listen.
Body friend central. Bill social sure.',1,'2024-07-24 08:28:33.676482',45);
INSERT INTO "admin_mentor_app_notification" VALUES (42,'Entire prepare into. Color range crime our. Still true ability themselves.
Before cultural green together interview tend drive.',1,'2024-07-24 08:28:33.759388',21);
INSERT INTO "admin_mentor_app_notification" VALUES (43,'Institution individual deal imagine indicate region different leave. Rate or money. Front sit your work plant off.
Test morning article attack fast continue event. Program behind number alone join.',1,'2024-07-24 08:28:33.925821',58);
INSERT INTO "admin_mentor_app_notification" VALUES (44,'Leader hear cause figure. Program arrive idea it tree onto situation. Although skill me movement hand since.
Black reflect win while home deal important. Republican century discussion pass federal.',1,'2024-07-24 08:28:34.130943',33);
INSERT INTO "admin_mentor_app_notification" VALUES (45,'Together painting value alone could maintain. Relationship no decade. Usually direction campaign Congress push modern young.
Out I artist. Put him local sing money.',0,'2024-07-24 08:28:34.270294',3);
INSERT INTO "admin_mentor_app_notification" VALUES (46,'Bar including even. Front free long hot. Discuss stay machine strong just. Culture final might.
Series hotel community two back better our. Day fly area parent.',1,'2024-07-24 08:28:34.386410',13);
INSERT INTO "admin_mentor_app_notification" VALUES (47,'Case establish cost buy develop bar last. Practice century go east trip election. Trip already employee grow.',1,'2024-07-24 08:28:34.590818',44);
INSERT INTO "admin_mentor_app_notification" VALUES (48,'Party enough risk whether board. Range statement religious force us development. Down adult coach represent section performance gas.',1,'2024-07-24 08:28:34.739791',55);
INSERT INTO "admin_mentor_app_notification" VALUES (49,'During professional enough accept stay much think environmental. Try wait side part west hold.',1,'2024-07-24 08:28:34.933836',31);
INSERT INTO "admin_mentor_app_notification" VALUES (50,'Matter ever stock decision sport. Reduce recent look audience generation set onto figure.
Adult possible six life see. Plan your participant sit I cause happen society.',1,'2024-07-24 08:28:35.108881',43);
INSERT INTO "admin_mentor_app_notification" VALUES (51,'Statement number PM main but tend. Have threat general. Fund cell change rock before training human bit.',0,'2024-07-24 08:28:35.266752',59);
INSERT INTO "admin_mentor_app_notification" VALUES (52,'Clearly relate fire marriage performance.
Opportunity fish civil. Old with left spring. Say statement stay performance Mrs particular fly oil.',0,'2024-07-24 08:28:35.390001',33);
INSERT INTO "admin_mentor_app_notification" VALUES (53,'Plant conference and perform entire matter some. Everybody always response long star street line. Often from reach institution name perform themselves.',0,'2024-07-24 08:28:35.554220',36);
INSERT INTO "admin_mentor_app_notification" VALUES (54,'Work fill him protect information task light result. Vote economic gas five world office score. Soldier suddenly myself imagine kitchen bag.',1,'2024-07-24 08:28:35.707406',10);
INSERT INTO "admin_mentor_app_notification" VALUES (55,'Gun go base sign this strong. Wish arrive attention. Free baby opportunity environmental certain size oil.
Accept nation into however his put money kind. Grow make free month.',0,'2024-07-24 08:28:35.874039',16);
INSERT INTO "admin_mentor_app_notification" VALUES (56,'Hard according east threat year. Work writer summer color information. Write pattern concern toward fast spring produce general.',0,'2024-07-24 08:28:36.019691',30);
INSERT INTO "admin_mentor_app_notification" VALUES (57,'Report heart heart that American life picture. Tv it ask information season eat. Family story yet occur lot hit.',1,'2024-07-24 08:28:36.187154',3);
INSERT INTO "admin_mentor_app_notification" VALUES (58,'A police team better court name. Vote require explain. Surface between soon decide. Pretty second mind start class.
Economy be later everybody think.
Several theory people culture ability beat.',1,'2024-07-24 08:28:36.321128',41);
INSERT INTO "admin_mentor_app_notification" VALUES (59,'A senior them general family science though. He wish east.
Sell nature door. First test senior area third. Matter physical identify garden piece sign.',1,'2024-07-24 08:28:36.500460',29);
INSERT INTO "admin_mentor_app_notification" VALUES (60,'Concern worker drive sit feeling pass party above. Administration choose population appear.
Create chair they always. Nice resource decade attack. Mrs above husband point.',0,'2024-07-24 08:28:36.672052',56);
INSERT INTO "admin_mentor_app_progress" VALUES (1,'Environment heart hot Congress.','1','5',17,26);
INSERT INTO "admin_mentor_app_progress" VALUES (2,'Spring different level become however.','0','8',5,28);
INSERT INTO "admin_mentor_app_progress" VALUES (3,'Late manager ever quality dark tough.','1','5',5,28);
INSERT INTO "admin_mentor_app_progress" VALUES (4,'West take black impact.','0','9',38,28);
INSERT INTO "admin_mentor_app_progress" VALUES (5,'Politics enter enough knowledge impact relationship.','1','5',38,28);
INSERT INTO "admin_mentor_app_progress" VALUES (6,'Most new oil special success fish hundred.','Completed','9',7,16);
INSERT INTO "admin_mentor_app_progress" VALUES (7,'Quickly trouble air easy dark deal.','Not Started','4',3,36);
INSERT INTO "admin_mentor_app_progress" VALUES (8,'Myself industry billion various themselves character international.','Not Started','6',30,21);
INSERT INTO "admin_mentor_app_progress" VALUES (9,'Four a decision off sell require parent.','Completed','8',41,21);
INSERT INTO "admin_mentor_app_progress" VALUES (10,'Low operation training issue far job.','In Progress','5',17,22);
INSERT INTO "admin_mentor_app_progress" VALUES (11,'School another sell hope.','Completed','7',45,55);
INSERT INTO "admin_mentor_app_progress" VALUES (12,'Heavy the prevent quickly.','In Progress','8',47,22);
INSERT INTO "admin_mentor_app_progress" VALUES (13,'Former opportunity article alone kid important risk.','In Progress','10',30,26);
INSERT INTO "admin_mentor_app_progress" VALUES (14,'Bed street down teach with.','In Progress','4',2,15);
INSERT INTO "admin_mentor_app_progress" VALUES (15,'Should think stay special behavior the.','Not Started','2',37,21);
INSERT INTO "admin_mentor_app_progress" VALUES (16,'Company many agency show cover form.','Completed','4',37,43);
INSERT INTO "admin_mentor_app_progress" VALUES (17,'Operation environmental teacher mission practice take ball.','In Progress','6',32,21);
INSERT INTO "admin_mentor_app_progress" VALUES (18,'Quality get able where really successful.','Not Started','2',41,22);
INSERT INTO "admin_mentor_app_progress" VALUES (19,'Not item education shake.','Completed','10',48,36);
INSERT INTO "admin_mentor_app_progress" VALUES (20,'Which unit charge lead music see business.','Not Started','9',12,43);
INSERT INTO "admin_mentor_app_progress" VALUES (21,'Company sea television church above.','Completed','5',35,16);
INSERT INTO "admin_mentor_app_progress" VALUES (22,'Court available song.','Not Started','4',33,49);
INSERT INTO "admin_mentor_app_progress" VALUES (23,'Actually born energy think hit truth become.','Not Started','7',60,50);
INSERT INTO "admin_mentor_app_progress" VALUES (24,'Break sound detail.','Not Started','7',23,22);
INSERT INTO "admin_mentor_app_progress" VALUES (25,'Case away time democratic.','Completed','3',7,13);
INSERT INTO "admin_mentor_app_progress" VALUES (26,'Fly fact world water nature boy.','1
','4',5,28);
INSERT INTO "admin_mentor_app_progress" VALUES (27,'Understand others baby dream fall represent.','In Progress','5',32,22);
INSERT INTO "admin_mentor_app_progress" VALUES (28,'Artist hot work southern sometimes bill both after.','Not Started','1',3,49);
INSERT INTO "admin_mentor_app_progress" VALUES (29,'No century behind successful of why day door.','Not Started','2',40,43);
INSERT INTO "admin_mentor_app_progress" VALUES (30,'Simply some decide keep he.','In Progress','6',48,16);
INSERT INTO "admin_mentor_app_progress" VALUES (31,'Here low view statement account soon.','In Progress','7',33,9);
INSERT INTO "admin_mentor_app_progress" VALUES (32,'She professional positive must and speech country.','Not Started','7',56,18);
INSERT INTO "admin_mentor_app_progress" VALUES (33,'Pressure season treat push.','In Progress','3',10,39);
INSERT INTO "admin_mentor_app_progress" VALUES (34,'Eat heart history sort option two others easy.','In Progress','1',58,22);
INSERT INTO "admin_mentor_app_progress" VALUES (35,'Gun TV from opportunity wife.','In Progress','3',41,21);
INSERT INTO "admin_mentor_app_progress" VALUES (36,'Half gun some although middle.','Completed','2',5,42);
INSERT INTO "admin_mentor_app_progress" VALUES (37,'Picture agency wrong every key every up.','Not Started','9',20,42);
INSERT INTO "admin_mentor_app_progress" VALUES (38,'Want build assume each.','Not Started','3',45,15);
INSERT INTO "admin_mentor_app_progress" VALUES (39,'Away cell office company.','In Progress','3',52,39);
INSERT INTO "admin_mentor_app_progress" VALUES (40,'President everyone record Mrs about degree crime.','1','6',38,28);
INSERT INTO "admin_mentor_app_progress" VALUES (41,'Skin enter fight worry cell foot night tell.','1','8',5,28);
INSERT INTO "admin_mentor_app_progress" VALUES (42,'Source project family always.','Not Started','1',45,39);
INSERT INTO "admin_mentor_app_progress" VALUES (43,'Product international industry possible particularly.','Completed','2',23,15);
INSERT INTO "admin_mentor_app_progress" VALUES (44,'Feeling live though really table today.','In Progress','2',35,49);
INSERT INTO "admin_mentor_app_progress" VALUES (45,'Coach owner nothing course claim.','Not Started','4',35,36);
INSERT INTO "admin_mentor_app_progress" VALUES (46,'Social some man maybe among.','In Progress','5',30,22);
INSERT INTO "admin_mentor_app_progress" VALUES (47,'Matter after year affect reveal bad experience.','Completed','4',52,49);
INSERT INTO "admin_mentor_app_progress" VALUES (48,'Operation difference bar professor.','Completed','7',33,9);
INSERT INTO "admin_mentor_app_progress" VALUES (49,'Beautiful especially southern group door fall cover.','Not Started','3',6,43);
INSERT INTO "admin_mentor_app_progress" VALUES (50,'Too check event administration end plan piece.','Completed','9',12,55);
INSERT INTO "admin_mentor_app_progress" VALUES (51,'Language Mrs raise black everyone.','Completed','2',33,26);
INSERT INTO "admin_mentor_app_progress" VALUES (52,'Beautiful attention its game follow.','Completed','3',30,55);
INSERT INTO "admin_mentor_app_progress" VALUES (53,'Throughout both name gas personal this certainly.','In Progress','5',23,39);
INSERT INTO "admin_mentor_app_progress" VALUES (54,'Just mind mother building walk.','Not Started','4',17,22);
INSERT INTO "admin_mentor_app_progress" VALUES (55,'What agency later image meet small road.','Completed','8',52,21);
INSERT INTO "admin_mentor_app_progress" VALUES (56,'Assume police sister positive base.','Not Started','7',5,55);
INSERT INTO "admin_mentor_app_progress" VALUES (57,'Country wish want amount maybe figure.','Completed','1',52,43);
INSERT INTO "admin_mentor_app_progress" VALUES (58,'Necessary food owner identify.','Not Started','4',3,18);
INSERT INTO "admin_mentor_app_progress" VALUES (59,'Concern than establish series development sit.','Completed','10',37,39);
INSERT INTO "admin_mentor_app_progress" VALUES (60,'Information least imagine including.','Not Started','4',48,43);
INSERT INTO "admin_mentor_app_schedule" VALUES (1,'2024-04-23 07:40:02.030894','scheduled',27,59);
INSERT INTO "admin_mentor_app_schedule" VALUES (2,'2024-03-26 09:02:53.115316','scheduled',51,60);
INSERT INTO "admin_mentor_app_schedule" VALUES (3,'2024-05-10 20:47:31.734040','canceled',60,23);
INSERT INTO "admin_mentor_app_schedule" VALUES (4,'2024-03-21 02:45:51.258291','canceled',47,19);
INSERT INTO "admin_mentor_app_schedule" VALUES (5,'2024-03-14 01:09:05.622256','canceled',32,41);
INSERT INTO "admin_mentor_app_schedule" VALUES (6,'2024-02-20 03:44:31.896049','completed',33,33);
INSERT INTO "admin_mentor_app_schedule" VALUES (7,'2024-02-20 21:12:06.874871','completed',53,15);
INSERT INTO "admin_mentor_app_schedule" VALUES (8,'2024-02-27 01:04:53.218524','confirmed',28,28);
INSERT INTO "admin_mentor_app_schedule" VALUES (9,'2024-01-28 18:38:10.094008','canceled',16,2);
INSERT INTO "admin_mentor_app_schedule" VALUES (10,'2024-07-19 00:29:20.267279','canceled',36,14);
INSERT INTO "admin_mentor_app_schedule" VALUES (11,'2024-01-12 05:40:18.572106','canceled',32,58);
INSERT INTO "admin_mentor_app_schedule" VALUES (12,'2024-01-04 14:50:49.781406','scheduled',3,56);
INSERT INTO "admin_mentor_app_schedule" VALUES (13,'2024-02-16 20:32:02.041294','scheduled',55,44);
INSERT INTO "admin_mentor_app_schedule" VALUES (14,'2024-02-01 02:13:28.825018','completed',16,35);
INSERT INTO "admin_mentor_app_schedule" VALUES (15,'2024-01-30 02:32:19.626230','confirmed',53,51);
INSERT INTO "admin_mentor_app_schedule" VALUES (16,'2024-07-05 16:14:03.276695','canceled',40,17);
INSERT INTO "admin_mentor_app_schedule" VALUES (17,'2024-01-31 06:04:07.198902','completed',18,19);
INSERT INTO "admin_mentor_app_schedule" VALUES (18,'2024-05-26 01:12:03.095641','confirmed',36,15);
INSERT INTO "admin_mentor_app_schedule" VALUES (19,'2024-05-19 03:44:22.514297','confirmed',54,16);
INSERT INTO "admin_mentor_app_schedule" VALUES (20,'2024-04-30 23:47:27.570668','confirmed',18,56);
INSERT INTO "admin_mentor_app_schedule" VALUES (21,'2024-07-12 11:10:59.346015','confirmed',59,17);
INSERT INTO "admin_mentor_app_schedule" VALUES (22,'2024-06-01 22:55:07.284360','scheduled',52,55);
INSERT INTO "admin_mentor_app_schedule" VALUES (23,'2024-04-20 17:26:06.801217','confirmed',18,32);
INSERT INTO "admin_mentor_app_schedule" VALUES (24,'2024-03-18 19:04:12.308399','canceled',23,2);
INSERT INTO "admin_mentor_app_schedule" VALUES (25,'2024-03-28 20:16:08.732262','completed',24,36);
INSERT INTO "admin_mentor_app_schedule" VALUES (26,'2024-02-29 16:29:08.913526','completed',35,18);
INSERT INTO "admin_mentor_app_schedule" VALUES (27,'2024-01-01 18:08:52.071780','scheduled',19,37);
INSERT INTO "admin_mentor_app_schedule" VALUES (28,'2024-01-26 13:20:30.837712','completed',46,24);
INSERT INTO "admin_mentor_app_schedule" VALUES (29,'2024-04-12 08:35:52.326126','canceled',39,57);
INSERT INTO "admin_mentor_app_schedule" VALUES (30,'2024-04-24 01:36:38.300536','confirmed',24,46);
INSERT INTO "admin_mentor_app_schedule" VALUES (31,'2024-03-22 02:11:47.231870','confirmed',2,11);
INSERT INTO "admin_mentor_app_schedule" VALUES (32,'2024-07-23 02:25:03.178163','confirmed',7,54);
INSERT INTO "admin_mentor_app_schedule" VALUES (33,'2024-06-09 21:59:27.563083','confirmed',59,57);
INSERT INTO "admin_mentor_app_schedule" VALUES (34,'2024-04-05 11:50:54.579387','completed',18,20);
INSERT INTO "admin_mentor_app_schedule" VALUES (35,'2024-01-13 15:07:13.276121','confirmed',20,15);
INSERT INTO "admin_mentor_app_schedule" VALUES (36,'2024-05-03 00:03:45.499539','completed',15,52);
INSERT INTO "admin_mentor_app_schedule" VALUES (37,'2024-05-15 09:10:58.546901','confirmed',51,54);
INSERT INTO "admin_mentor_app_schedule" VALUES (38,'2024-05-10 00:09:28.025768','completed',8,31);
INSERT INTO "admin_mentor_app_schedule" VALUES (39,'2024-03-25 01:36:59.201312','canceled',26,13);
INSERT INTO "admin_mentor_app_schedule" VALUES (40,'2024-01-15 12:20:28.436419','confirmed',25,4);
INSERT INTO "admin_mentor_app_schedule" VALUES (41,'2024-03-08 03:47:46.165801','scheduled',43,42);
INSERT INTO "admin_mentor_app_schedule" VALUES (42,'2024-03-31 21:12:13.649045','canceled',10,54);
INSERT INTO "admin_mentor_app_schedule" VALUES (43,'2024-07-14 05:34:43.206402','scheduled',27,44);
INSERT INTO "admin_mentor_app_schedule" VALUES (44,'2024-06-13 10:10:34.784356','canceled',10,9);
INSERT INTO "admin_mentor_app_schedule" VALUES (45,'2024-06-24 22:08:54.751522','scheduled',5,49);
INSERT INTO "admin_mentor_app_schedule" VALUES (46,'2024-01-06 20:37:33.612721','scheduled',35,5);
INSERT INTO "admin_mentor_app_schedule" VALUES (47,'2024-07-21 16:45:04.574138','scheduled',35,58);
INSERT INTO "admin_mentor_app_schedule" VALUES (48,'2024-02-14 10:33:49.160563','scheduled',3,24);
INSERT INTO "admin_mentor_app_schedule" VALUES (49,'2024-06-11 03:48:59.375974','completed',13,38);
INSERT INTO "admin_mentor_app_schedule" VALUES (50,'2024-02-15 14:50:03.758046','canceled',2,20);
INSERT INTO "admin_mentor_app_schedule" VALUES (51,'2024-06-05 02:29:38.415662','completed',12,41);
INSERT INTO "admin_mentor_app_schedule" VALUES (52,'2024-01-13 15:47:32.751134','canceled',4,41);
INSERT INTO "admin_mentor_app_schedule" VALUES (53,'2024-04-20 07:41:40.433157','scheduled',59,21);
INSERT INTO "admin_mentor_app_schedule" VALUES (54,'2024-04-15 21:54:42.912591','confirmed',59,3);
INSERT INTO "admin_mentor_app_schedule" VALUES (55,'2024-02-19 12:51:10.118364','confirmed',5,36);
INSERT INTO "admin_mentor_app_schedule" VALUES (56,'2024-03-31 20:34:23.937073','confirmed',15,4);
INSERT INTO "admin_mentor_app_schedule" VALUES (57,'2024-01-09 23:40:05.154772','confirmed',49,60);
INSERT INTO "admin_mentor_app_schedule" VALUES (58,'2024-02-18 13:43:46.650929','canceled',57,29);
INSERT INTO "admin_mentor_app_schedule" VALUES (59,'2024-06-27 21:18:17.946720','completed',43,7);
INSERT INTO "admin_mentor_app_schedule" VALUES (60,'2024-03-29 05:48:29.782258','canceled',35,44);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Megan','Chang','gwilliams@example.com','Female','Uruguay','1992-12-08','pbkdf2_sha256$600000$53PbhoZZBj5FL5KFtpdvQD$CyhxiKfa3l5nf09EGKbFpah3mgBg2/I6XXRqt5MrHSQ=','475-693-8242x1948','1','',1);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Jessica','Nolan','thomas15@example.com','Female','New Zealand','1983-11-27','pbkdf2_sha256$600000$1u6Je0EyaXKhQy1FAVrWGu$AXa0Dtc8QMK00eUaBZfs06b3KPvCbx1rWgt34Ph1E2I=','387.878.4080','3','',2);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Mallory','Barnett','salazarmaria@example.com','Male','Saint Lucia','1964-01-18','pbkdf2_sha256$600000$S7qsCZ6Aswi1aILfomddSR$3GdU1Mt6CuxNqmZHz0euaBB4+iJx00RCrkhqo3SL8BE=','339-733-2871','3','',3);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Whitney','Burns','andrea18@example.com','Male','South Georgia and the South Sandwich Islands','1981-07-23','pbkdf2_sha256$600000$i2LoRXb2cPByXZZ53TufbA$AuC9Nn7rZ9FfWX1RD2uD+/wV0SOVd0M+Y16qD463DHQ=','001-647-419-6593','1','',4);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Lori','Johnson','thomas12@example.org','Male','Tajikistan','1948-08-12','pbkdf2_sha256$600000$XhL8TFf86pnSgZEyKUnmSq$vULyjS9MT12j09btf4v0JPw0FSNl6Z0SZ6ckaOFjw2k=','001-986-984-8339x694','3','',5);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Danielle','Graves','christopher91@example.com','Female','Tanzania','1955-07-21','pbkdf2_sha256$600000$btAC0g4vJcAwjBOdpPpi5t$Ix8J8mWfkzv4j2j8HWOeLgheVaphp6qPNiaAx26X5JU=','3414352560','3','',6);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Jeffery','Montoya','johnsoncynthia@example.net','Male','India','1949-04-29','pbkdf2_sha256$600000$lRes2dfrUqyXLkGEj1zjZk$0g6ewJv9JhfCrkv2ejE04Jw6zec9f/jV6MWBIlDdqls=','209-203-2173','3','',7);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Ronald','Garcia','chad14@example.com','Female','Cocos (Keeling) Islands','1947-05-28','pbkdf2_sha256$600000$y6tCnQ29d6eHOIUsvVj2fG$TEdsA6qa0/f/AU+dwB7Pi/hE2RS7z4SIMyxo+2JE+4M=','209.416.3457x923','1','',8);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Matthew','King','awade@example.com','Female','United Arab Emirates','1979-05-31','pbkdf2_sha256$600000$D0Vm5AvURThWhJEs3RrBSA$sdQ34slZE5gnTNUVx6ltF+oAf931G4BlCyUXedQdNPg=','445.564.2807x15084','2','',9);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Michael','Roberts','brittany92@example.net','Female','Iceland','1990-09-18','pbkdf2_sha256$600000$9lrnotHmcBH24CTPP2JptN$bIiObtwz4BpDk6O4mOku9r0mmKELBWi8glW9yKTvAow=','+1-210-893-5233x7696','3','',10);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Ashley','Barton','martincaleb@example.net','Male','Kiribati','1976-10-17','pbkdf2_sha256$600000$xMWMZn7zBV6BcqnloIkpDW$hI1vQUC4AdotyFvlo5xiPX6E2/SOiWuU7hm4TlvLFR0=','389.400.7547x0638','1','',11);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Richard','Gregory','aaron00@example.net','Male','Comoros','1951-01-19','pbkdf2_sha256$600000$PtBaaor3ZPD3eaoNjNvt3P$65G+cj2WjUbFdxKLv5hs8XoEvTHsJHN34kkgKgwmGso=','+1-634-442-1761x0471','3','',12);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Abigail','Curtis','darin24@example.org','Male','Armenia','1956-07-09','pbkdf2_sha256$600000$KZqa1aXz4XdoBncSeX62mj$nTPGE6s2i+1MmljJwfTU6La4N5rq8sLEmTABRZevvZs=','485-559-0977x658','2','',13);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Brenda','Smith','josephmorgan@example.com','Male','Guadeloupe','1992-08-30','pbkdf2_sha256$600000$ToCiFEp4wpg07kHrf9E3dp$KLhhn9y6uSm9gq7X+rpgm7BsOheH9CACSaHg7DhAtK4=','4046229456','1','',14);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Timothy','Allen','parkermelody@example.net','Male','Gabon','1968-12-16','pbkdf2_sha256$600000$l5KStxqR1mQMG1pITQavvL$W67pMWAtT5wYi0bKH9fhIf4VBJlSnQwk4bNPchR8i8o=','846-211-8775x51717','2','',15);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Matthew','Mcdaniel','samanthasims@example.com','Male','Bahrain','1994-06-13','pbkdf2_sha256$600000$bsCkbMRhZolEhzsDgx4CgN$tGMelgycPrGCTy8PI0vxjxRMDCBPc7KIfug13CNwn0E=','630.960.1688','2','',16);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Kristina','Klein','rodneyrichardson@example.com','Male','Jersey','1955-08-26','pbkdf2_sha256$600000$usDfN0CXdPsAkfas7zhSXY$ShnEo8UxExH2myPqL/ZZ8ws3DvsCZupkAyVW754ZSI4=','610-587-3176','3','',17);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Bobby','Gould','cindygarcia@example.com','Female','Guyana','1977-12-25','pbkdf2_sha256$600000$QS1DL0SjSf4rFCjEdODH6n$JUKDc+lM8wjxJ760kUDk9SGe7tcPVPYGLsXZccfWLXE=','(919)772-9668','2','',18);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Whitney','Reid','amyvelazquez@example.org','Female','Romania','2004-03-14','pbkdf2_sha256$600000$a7FnIrpUPr1HqYXXarbtXy$8q85Z//8sxeBRf0TMZWIJk4rg43LrVIqgB5cQ7BsTk4=','250-382-4926x94711','1','',19);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'David','Turner','krivera@example.org','Female','Holy See (Vatican City State)','1975-05-17','pbkdf2_sha256$600000$rqaeseN8GHgcW3bb1Z2kCP$WotWHAr6cZXe8B7qWwgVc2gPKIJ8DtKb/Reb5gOmYjw=','980.891.8916x34896','3','',20);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Brenda','York','sandovalaaron@example.org','Female','Madagascar','1979-06-27','pbkdf2_sha256$600000$1gNKAikXjbmLrhVgoyQbCa$rpihpGXXmuM/QWAaKKA3lPKO8TrhD4n6I27XIC9NRds=','217-244-6660x22345','2','',21);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Robert','Vasquez','nunezedward@example.com','Female','Argentina','1982-02-06','pbkdf2_sha256$600000$Cpiwv2cdWZfMp6I2I2nnLg$OXEJ8b7g5c47QXgxrw/QHRuSkttvUHSVqGuV78svt0Y=','(770)517-2009x9251','2','',22);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Krista','Waters','ibarrachelsea@example.com','Female','Pakistan','1951-05-23','pbkdf2_sha256$600000$lAU7eZmvJa4ZRmgdWYkTXc$DHZI24ZtsSHdCWz2D7Aqg2NIE2aLu1RhFVYs7vmPTRY=','+1-994-726-4183x06753','3','',23);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Charles','Williams','tuckerrachel@example.net','Male','Denmark','1949-06-12','pbkdf2_sha256$600000$CQzVzsDllxWsLXxtBJGNa9$+TpaP2DeSDDNBeQh5elo3cQUvK+JA2pU8mpyQAc21+4=','+1-888-368-4126x9611','1','',24);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Robert','Moore','moodyryan@example.com','Male','Luxembourg','2001-06-22','pbkdf2_sha256$600000$lft8Sm4q4kzCBEUDp0kglF$P24ZA/xCRVvG7BD4jT5DTyQHO5Bn86rL2Gxft7VbuYo=','341-451-1505x52035','1','',25);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Aaron','Hopkins','adkinskelly@example.net','Male','Venezuela','1981-08-31','pbkdf2_sha256$600000$WBEn60VVpLfY06c9JQ48Mu$oMX3V78wbd128xQ6nV+cDEQDECHOcu5F69ksi+VEX7A=','(527)717-5420','2','',26);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Thomas','Carter','jack11@example.net','Female','Cayman Islands','1967-04-14','pbkdf2_sha256$600000$wHA7AbbAvy6hScCzSAgiFL$qwfY+8hMiyJpzrGRshpO/9iv4lLaJBA9VdGuexF493Y=','(723)858-3324','3','',27);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Brandon','Anderson','longjacqueline@example.org','Female','French Southern Territories','1978-04-04','pbkdf2_sha256$600000$lhPOWUVKQsGR8NdS972nCn$fN2m0C7/UdTENNZC1DeNYQo5GnDumZTVf03+WMrRO68=','001-829-264-5137x5806','2','',28);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Suzanne','Valenzuela','sharris@example.com','Male','Zambia','1955-03-30','pbkdf2_sha256$600000$v2cfSyTBZOOpJZRydy9gh1$irGy7hs4kl2/oO9jJTySnHL24zOpsP4T1imnMZBuJPI=','841-889-2762','1','',29);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'John','Chavez','michaelwelch@example.org','Female','Saudi Arabia','1956-05-21','pbkdf2_sha256$600000$0vwNoVnOyOpbHuhSRji8wh$72HgiRvkMvUEcHCs637B1vK/TYPoBfQTCrBPwSkhpEE=','4798703414','3','',30);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Karen','Davis','owolf@example.net','Female','Fiji','1983-05-19','pbkdf2_sha256$600000$ndOqI7LPR3jLxImQQpcQTP$jm2fTl36W3hme5bKjcSRTCQ3fd05ygD3/hEDZgzTAUY=','8149004689','1','',31);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Julie','Gomez','caitlinjohnson@example.com','Female','Martinique','1964-12-21','pbkdf2_sha256$600000$Ni2C7LO7jRdF5dAegaAbmt$hDD61RnimsX5m3l7xLrMuaICWlRBj/4ERx76elEm6iE=','832.816.4482x98381','3','',32);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Kimberly','French','scott92@example.org','Male','Qatar','1951-02-25','pbkdf2_sha256$600000$MQ4UxSmS9m4UvvxqV5Lj9P$j3D/SgtH9zbPEyG+1hcE+0X1PHF7nXMAaQxd5o50+fk=','(797)928-4576x3778','3','',33);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Susan','Wallace','juliewilliams@example.net','Male','Anguilla','1965-12-13','pbkdf2_sha256$600000$rOVMS59Xunnl5vgB3OYsya$lYrG5NP1R++uw/KAa9B5pyg/U4VZh7L5eK+ofOdCDRM=','(608)511-6050x1904','1','',34);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Karen','Roberts','hamiltonjennifer@example.com','Male','Greenland','1970-02-15','pbkdf2_sha256$600000$rtdAHZhpPcVAOnS0F2Xny3$U7iPe0iUa54nzNXgoXrhQVc/iWRkh5A4MOlCybry9wY=','+1-962-872-8523x27566','3','',35);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Jeffrey','Gonzalez','brendawilliams@example.com','Male','Djibouti','1983-06-14','pbkdf2_sha256$600000$GNtt3VvIgCbiFf7psEWmld$Rv4P62aPYuk+vxFkHAD7k+MlAHQOlDxIB+2c5v/7EUY=','(650)723-9491','2','',36);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Stephen','Welch','fcarpenter@example.com','Female','Cuba','1964-10-20','pbkdf2_sha256$600000$PAuXsBILUn5qa7AbPTnRvm$OiQ6VgSGdRzaQzpyje2deqwZx42SxURQ4T4wAOk9u54=','3008250402','3','',37);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Jeffrey','Franklin','shawnmorgan@example.org','Male','South Africa','1963-08-29','pbkdf2_sha256$600000$5OYdDFX3wL21PugvQYnI4L$witKybvkA1OXOdwYjckYMJLpmLWBIGfnAupjr52AgKs=','+1-375-540-8035','3','',38);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Michael','Hood','emily44@example.net','Female','Equatorial Guinea','1973-12-06','pbkdf2_sha256$600000$Lshv3WzXuL4Qw0l6P1F7g2$NsPgv+QOSll6KbBNIJbtrUogaupEeFiPQp0IAd0jbXo=','001-930-948-1077x706','2','',39);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'David','Miller','mckenzieeric@example.org','Female','New Zealand','1948-06-02','pbkdf2_sha256$600000$mo2qFTJVZV25piaJz9VmB6$9tuEEj9bwYO3t/uGNJAco0psPI97BnUuZq4FJ7rQTOw=','(686)502-3732x45561','3','',40);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Kenneth','Ramos','qherrera@example.com','Male','Andorra','1951-01-15','pbkdf2_sha256$600000$1TLAGf4bSOr3TWBNMM8S4f$CogZAhYcThC7o9rYFBnnt0ecaw7qqIh9nWP6uPHGgSc=','001-312-863-3408x860','3','',41);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Joseph','Maddox','jerome84@example.org','Male','Bahrain','1976-03-15','pbkdf2_sha256$600000$bjUPeSeVTMdLq0xNQLzYnn$2F4LU/GuRDEz3OWawV/6z0ezFsMdL7DEW8h0nhgZtvM=','+1-253-457-4922x08855','2','',42);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Eric','Thompson','taylorjamie@example.com','Male','Dominica','1989-09-16','pbkdf2_sha256$600000$Qgrm3JDUmc71fslpdgJvIW$vsWqqLVVE1vLusS793HM0/26OF4SUhnCvGL6abxI/w0=','265.799.2719','2','',43);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Stanley','Smith','angelamartin@example.com','Female','Mayotte','1963-05-04','pbkdf2_sha256$600000$DZyVXzqEWzJ5Dby4by9GGL$MmdywJJinTep9ykl+dez80vxy3OAUXMQbFBJN1+14zk=','242-596-3546','1','',44);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Leslie','Burgess','matthewalexander@example.net','Male','Eritrea','1965-03-29','pbkdf2_sha256$600000$eRl4JNKLhzlkmVB5n2NqO9$DO5AMU79quIa9OXhx0bByVQgKFGIauwf7gpQBhNy3/M=','(240)959-8025','3','',45);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Bryan','Allen','perezdesiree@example.org','Male','Guatemala','2004-10-19','pbkdf2_sha256$600000$uqGg6fgsYVDI8iEKHhJxiS$0XEuGREa4q+Ujmi8SoTayz/BvlWZ/dFUuwUsDZmZYeM=','(623)976-2542x56606','1','',46);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Annette','Martinez','gjackson@example.org','Male','Belgium','1964-05-08','pbkdf2_sha256$600000$rdJvSUxBXL92EYrkYSGbkF$ihkCGT5VxHnWuNfHc3hkS/3IPIs5jWpjSdr1UI3V6Kw=','(330)928-2169','3','',47);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Edward','Guzman','matthew60@example.net','Male','Luxembourg','1949-03-16','pbkdf2_sha256$600000$rCu6ynDTVo9UW4WApvr1Jg$hyj88oVJzvUBD8CVhJipr/Ujf0IN+t9iSXRVRx5kbiU=','627-638-5265x4760','3','',48);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Taylor','Johnson','sarah07@example.com','Male','Iraq','1965-05-24','pbkdf2_sha256$600000$cXUZu2RPM24uyyehLV1jNb$16H7MSzFd2uofYtQj8V6abkbO9kbN5842y8ByLGXmJg=','7048049438','2','',49);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Jason','Knight','linda39@example.net','Female','Central African Republic','2001-04-16','pbkdf2_sha256$600000$HxYVYXVwyACIgELs94d3T0$FduKSkorNY6W87AKpQXcCvnnmGFp8Abxr6lMheBf/Iw=','(650)690-9255','2','',50);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Troy','Powell','aarcher@example.org','Male','Kenya','1951-06-27','pbkdf2_sha256$600000$6RfokQbUEGdwaINnye84Hz$3+2eZ66qVfr5l2xi1uR+PXEef99uq5LjR05fWnsO6aU=','4744931864','1','',51);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Donna','Moore','davidcrystal@example.net','Female','Saudi Arabia','1970-12-10','pbkdf2_sha256$600000$OHLRHVC0ydBR7Wvx3dPpDi$f9Z6iKmiHIUnBFhA9gPznxwhFnf2o7LJ7RWtpD/6fVk=','440-264-4888x5536','3','',52);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Eric','Guerrero','cward@example.net','Female','North Macedonia','1982-04-01','pbkdf2_sha256$600000$kuVk6q6RCXnniXkzoJKtz8$/hTjL5HkRloYJ2CAcPz1/1SK4vfDshsQU+Kyom5f2Gs=','001-430-858-2357x03934','1','',53);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Ashley','Young','zshields@example.net','Male','Comoros','1953-12-02','pbkdf2_sha256$600000$CUlZQBVjSwJe8LQpLzh7Ay$yHA7bWPiAltQYJ1+BLoC5zoi1oizoyFjbnD14w71tPs=','366-644-6595','1','',54);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Travis','Farmer','kathrynhughes@example.net','Female','Qatar','1999-01-04','pbkdf2_sha256$600000$vrZiOQ0e4ziP7hFrhCMJLQ$lv9LnDY4SeZzdmZNJbkr3zBKExj1EQEUTjFKiRecR8M=','2978592945','2','',55);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Samantha','Taylor','knightmichael@example.org','Male','Comoros','1988-09-30','pbkdf2_sha256$600000$pCT2ZTOxtHK3mbwZFWFrTC$JYuPqJIRmv68yM2FtSIQjGbPkmkOn1Ta3N/nRq5HGbA=','+1-887-605-0562x46292','3','',56);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Brian','Martinez','reneethornton@example.net','Male','Saint Lucia','1995-06-16','pbkdf2_sha256$600000$8NzES0R5UvOxgtvMVvRxmc$jv0wT6TXpKmrlHceoN9f/1yFfLRNOkqXhLRxVuEw0hk=','4866259118','1','',57);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Lauren','Murphy','kimberly87@example.org','Female','Micronesia','1953-03-09','pbkdf2_sha256$600000$o1VmFS0qRA4Zz2C4xft2Lu$CmttBQYSsM3vcz9Uh2cFx/As+sV1lxiS6sQ6aw39pc8=','+1-492-780-5137x9378','3','',58);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Dennis','Ingram','stephenslori@example.com','Male','Suriname','1992-05-17','pbkdf2_sha256$600000$6JHWZ8ArHpLa9bm98VYtVe$A4gAixHQA58DwjE9nhNQ1ABfi4nhKxkOElyXHQ5a3xQ=','769-359-7568','1','',59);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'Logan','Johnson','andrewblackwell@example.org','Male','Isle of Man','1984-03-21','pbkdf2_sha256$600000$JEqJqWQtoDilVkgl93pE4Y$tOPrPPqwll7DDdOvPBh7qqBwHiaaP7yBTblezt6prWo=','001-646-609-2516x075','3','',60);
INSERT INTO "admin_mentor_app_user" VALUES (NULL,0,'David','Oliver','cury@mailinator.com','M','Mollit beatae pariatur Vel odit odio non facilis','1990-12-01','Pa$$w0rd!','+1 (922) 874-7','3','',61);
INSERT INTO "admin_mentor_app_user" VALUES ('2024-07-24 08:31:58.032871',0,'admin','userAdmin','admin@gmail.com','M','Nisi qui consequatur commodo pariatur Debitis','2024-07-10','12345','0763469896','3','',62);
INSERT INTO "auth_permission" VALUES (1,1,'add_user','Can add user');
INSERT INTO "auth_permission" VALUES (2,1,'change_user','Can change user');
INSERT INTO "auth_permission" VALUES (3,1,'delete_user','Can delete user');
INSERT INTO "auth_permission" VALUES (4,1,'view_user','Can view user');
INSERT INTO "auth_permission" VALUES (5,2,'add_schedule','Can add schedule');
INSERT INTO "auth_permission" VALUES (6,2,'change_schedule','Can change schedule');
INSERT INTO "auth_permission" VALUES (7,2,'delete_schedule','Can delete schedule');
INSERT INTO "auth_permission" VALUES (8,2,'view_schedule','Can view schedule');
INSERT INTO "auth_permission" VALUES (9,3,'add_progress','Can add progress');
INSERT INTO "auth_permission" VALUES (10,3,'change_progress','Can change progress');
INSERT INTO "auth_permission" VALUES (11,3,'delete_progress','Can delete progress');
INSERT INTO "auth_permission" VALUES (12,3,'view_progress','Can view progress');
INSERT INTO "auth_permission" VALUES (13,4,'add_notification','Can add notification');
INSERT INTO "auth_permission" VALUES (14,4,'change_notification','Can change notification');
INSERT INTO "auth_permission" VALUES (15,4,'delete_notification','Can delete notification');
INSERT INTO "auth_permission" VALUES (16,4,'view_notification','Can view notification');
INSERT INTO "auth_permission" VALUES (17,5,'add_message','Can add message');
INSERT INTO "auth_permission" VALUES (18,5,'change_message','Can change message');
INSERT INTO "auth_permission" VALUES (19,5,'delete_message','Can delete message');
INSERT INTO "auth_permission" VALUES (20,5,'view_message','Can view message');
INSERT INTO "auth_permission" VALUES (21,6,'add_mentorshipmatch','Can add mentorship match');
INSERT INTO "auth_permission" VALUES (22,6,'change_mentorshipmatch','Can change mentorship match');
INSERT INTO "auth_permission" VALUES (23,6,'delete_mentorshipmatch','Can delete mentorship match');
INSERT INTO "auth_permission" VALUES (24,6,'view_mentorshipmatch','Can view mentorship match');
INSERT INTO "auth_permission" VALUES (25,7,'add_evaluation','Can add evaluation');
INSERT INTO "auth_permission" VALUES (26,7,'change_evaluation','Can change evaluation');
INSERT INTO "auth_permission" VALUES (27,7,'delete_evaluation','Can delete evaluation');
INSERT INTO "auth_permission" VALUES (28,7,'view_evaluation','Can view evaluation');
INSERT INTO "auth_permission" VALUES (29,8,'add_permission','Can add permission');
INSERT INTO "auth_permission" VALUES (30,8,'change_permission','Can change permission');
INSERT INTO "auth_permission" VALUES (31,8,'delete_permission','Can delete permission');
INSERT INTO "auth_permission" VALUES (32,8,'view_permission','Can view permission');
INSERT INTO "auth_permission" VALUES (33,9,'add_group','Can add group');
INSERT INTO "auth_permission" VALUES (34,9,'change_group','Can change group');
INSERT INTO "auth_permission" VALUES (35,9,'delete_group','Can delete group');
INSERT INTO "auth_permission" VALUES (36,9,'view_group','Can view group');
INSERT INTO "auth_permission" VALUES (37,10,'add_contenttype','Can add content type');
INSERT INTO "auth_permission" VALUES (38,10,'change_contenttype','Can change content type');
INSERT INTO "auth_permission" VALUES (39,10,'delete_contenttype','Can delete content type');
INSERT INTO "auth_permission" VALUES (40,10,'view_contenttype','Can view content type');
INSERT INTO "auth_permission" VALUES (41,11,'add_logentry','Can add log entry');
INSERT INTO "auth_permission" VALUES (42,11,'change_logentry','Can change log entry');
INSERT INTO "auth_permission" VALUES (43,11,'delete_logentry','Can delete log entry');
INSERT INTO "auth_permission" VALUES (44,11,'view_logentry','Can view log entry');
INSERT INTO "auth_permission" VALUES (45,12,'add_session','Can add session');
INSERT INTO "auth_permission" VALUES (46,12,'change_session','Can change session');
INSERT INTO "auth_permission" VALUES (47,12,'delete_session','Can delete session');
INSERT INTO "auth_permission" VALUES (48,12,'view_session','Can view session');
INSERT INTO "django_content_type" VALUES (1,'admin_mentor_app','user');
INSERT INTO "django_content_type" VALUES (2,'admin_mentor_app','schedule');
INSERT INTO "django_content_type" VALUES (3,'admin_mentor_app','progress');
INSERT INTO "django_content_type" VALUES (4,'admin_mentor_app','notification');
INSERT INTO "django_content_type" VALUES (5,'admin_mentor_app','message');
INSERT INTO "django_content_type" VALUES (6,'admin_mentor_app','mentorshipmatch');
INSERT INTO "django_content_type" VALUES (7,'admin_mentor_app','evaluation');
INSERT INTO "django_content_type" VALUES (8,'auth','permission');
INSERT INTO "django_content_type" VALUES (9,'auth','group');
INSERT INTO "django_content_type" VALUES (10,'contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES (11,'admin','logentry');
INSERT INTO "django_content_type" VALUES (12,'sessions','session');
INSERT INTO "django_migrations" VALUES (1,'contenttypes','0001_initial','2024-07-24 08:23:26.452692');
INSERT INTO "django_migrations" VALUES (2,'contenttypes','0002_remove_content_type_name','2024-07-24 08:23:26.546966');
INSERT INTO "django_migrations" VALUES (3,'auth','0001_initial','2024-07-24 08:23:26.863303');
INSERT INTO "django_migrations" VALUES (4,'auth','0002_alter_permission_name_max_length','2024-07-24 08:23:26.997529');
INSERT INTO "django_migrations" VALUES (5,'auth','0003_alter_user_email_max_length','2024-07-24 08:23:27.162245');
INSERT INTO "django_migrations" VALUES (6,'auth','0004_alter_user_username_opts','2024-07-24 08:23:27.295771');
INSERT INTO "django_migrations" VALUES (7,'auth','0005_alter_user_last_login_null','2024-07-24 08:23:27.349759');
INSERT INTO "django_migrations" VALUES (8,'auth','0006_require_contenttypes_0002','2024-07-24 08:23:27.504925');
INSERT INTO "django_migrations" VALUES (9,'auth','0007_alter_validators_add_error_messages','2024-07-24 08:23:27.678361');
INSERT INTO "django_migrations" VALUES (10,'auth','0008_alter_user_username_max_length','2024-07-24 08:23:27.837505');
INSERT INTO "django_migrations" VALUES (11,'auth','0009_alter_user_last_name_max_length','2024-07-24 08:23:27.963253');
INSERT INTO "django_migrations" VALUES (12,'auth','0010_alter_group_name_max_length','2024-07-24 08:23:28.030065');
INSERT INTO "django_migrations" VALUES (13,'auth','0011_update_proxy_permissions','2024-07-24 08:23:28.223140');
INSERT INTO "django_migrations" VALUES (14,'auth','0012_alter_user_first_name_max_length','2024-07-24 08:23:28.385677');
INSERT INTO "django_migrations" VALUES (15,'admin_mentor_app','0001_initial','2024-07-24 08:23:28.799007');
INSERT INTO "django_migrations" VALUES (16,'admin','0001_initial','2024-07-24 08:29:22.473449');
INSERT INTO "django_migrations" VALUES (17,'admin','0002_logentry_remove_auto_add','2024-07-24 08:29:22.577842');
INSERT INTO "django_migrations" VALUES (18,'admin','0003_logentry_add_action_flag_choices','2024-07-24 08:29:22.780565');
INSERT INTO "django_migrations" VALUES (19,'sessions','0001_initial','2024-07-24 08:29:23.090181');
INSERT INTO "django_session" VALUES ('imiotcnluzk1tpoq4n5ykczkd1oi55ck','.eJxVizsOwjAQBe_iGkX-r02JlHNYG9srW2AT5VMh7k6QUkDzijczLxZw30rY17yEmtiVWckuv-eE8Z77l2BqtYeW-_ZcAs7zcKJ1GBvWx-0U_-qCazlSg2S9AwIu-EQSVBZJSaOMV5FLmlIGKTS3x4IjoTVoRCDPKUWlrWPvD0qzNkE:1sWXPi:Sq3djc95j4xHs_ks7TuTitVnPBBxr2g2HzXhGBQ7y-Q','2024-08-07 08:31:58.125237');
CREATE INDEX IF NOT EXISTS "admin_mentor_app_evaluation_mentee_id_376410b3" ON "admin_mentor_app_evaluation" (
	"mentee_id"
);
CREATE INDEX IF NOT EXISTS "admin_mentor_app_evaluation_mentor_id_2181e3a8" ON "admin_mentor_app_evaluation" (
	"mentor_id"
);
CREATE INDEX IF NOT EXISTS "admin_mentor_app_evaluation_mentorship_match_id_e53877db" ON "admin_mentor_app_evaluation" (
	"mentorship_match_id"
);
CREATE INDEX IF NOT EXISTS "admin_mentor_app_mentorshipmatch_mentee_id_a96fcc65" ON "admin_mentor_app_mentorshipmatch" (
	"mentee_id"
);
CREATE INDEX IF NOT EXISTS "admin_mentor_app_mentorshipmatch_mentor_id_c52c42b6" ON "admin_mentor_app_mentorshipmatch" (
	"mentor_id"
);
CREATE INDEX IF NOT EXISTS "admin_mentor_app_message_receiver_id_abd6e43e" ON "admin_mentor_app_message" (
	"receiver_id"
);
CREATE INDEX IF NOT EXISTS "admin_mentor_app_message_sender_id_1158a737" ON "admin_mentor_app_message" (
	"sender_id"
);
CREATE INDEX IF NOT EXISTS "admin_mentor_app_notification_user_id_31d91490" ON "admin_mentor_app_notification" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "admin_mentor_app_progress_mentee_id_77adfeb2" ON "admin_mentor_app_progress" (
	"mentee_id"
);
CREATE INDEX IF NOT EXISTS "admin_mentor_app_progress_mentor_id_e6e6bc40" ON "admin_mentor_app_progress" (
	"mentor_id"
);
CREATE INDEX IF NOT EXISTS "admin_mentor_app_schedule_mentee_id_28850284" ON "admin_mentor_app_schedule" (
	"mentee_id"
);
CREATE INDEX IF NOT EXISTS "admin_mentor_app_schedule_mentor_id_748d3dcc" ON "admin_mentor_app_schedule" (
	"mentor_id"
);
CREATE INDEX IF NOT EXISTS "admin_mentor_app_user_groups_group_id_4aa4e1a2" ON "admin_mentor_app_user_groups" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "admin_mentor_app_user_groups_user_id_7ebf8aa0" ON "admin_mentor_app_user_groups" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "admin_mentor_app_user_groups_user_id_group_id_ef8ae651_uniq" ON "admin_mentor_app_user_groups" (
	"user_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "admin_mentor_app_user_user_permissions_permission_id_2f713868" ON "admin_mentor_app_user_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "admin_mentor_app_user_user_permissions_user_id_196f47ed" ON "admin_mentor_app_user_user_permissions" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "admin_mentor_app_user_user_permissions_user_id_permission_id_91132826_uniq" ON "admin_mentor_app_user_user_permissions" (
	"user_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
COMMIT;
